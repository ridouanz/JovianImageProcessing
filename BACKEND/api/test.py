import cv2 as cv
from fastapi import FastAPI, UploadFile
import pathlib
import os
import sys
from fastapi.middleware.cors import CORSMiddleware

from fastapi import FastAPI, File, Request
from datetime import datetime
import numpy as np

from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse

parent_path = pathlib.Path(os.path.realpath(__file__)).parent.parent
sys.path.append(str(parent_path))

from src import ImageLoader, ImageProcessor

parent_path = pathlib.Path(os.path.realpath(__file__)).parent.parent.parent
sys.path.append(str(parent_path))
app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
app.mount("/assets", StaticFiles(directory="assets"), name="assets")

#fix the Cross-Origin Resource Sharing with angular
origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#@app.get("/")
#def read_root():
#    return {"msg": "Hello :)"}


@app.get("/")
def get_app_angular():
    with open('static/index.html', 'r') as file_index:
        html_content = file_index.read()
    return HTMLResponse(html_content, status_code=200)


@app.post("/process")
async def getInformation(info : Request):
    req_info = await info.json()
    img_id=req_info["img"]
    img_raw = ImageLoader(id = img_id).load()
    img_processed = ImageProcessor(id = img_id).enhance()
    
    #cv.imwrite(f"{str(parent_path)}/FRONTEND/src/assets/imgs/{img_id}.png", img_raw)
    #cv.imwrite(f"{str(parent_path)}/FRONTEND/src/assets/processed_imgs/{img_id}_processed.png", img_processed)

    cv.imwrite(f"{str(parent_path)}/BACKEND/api/assets/imgs/{img_id}.png", img_raw)
    cv.imwrite(f"{str(parent_path)}/BACKEND/api/assets/processed_imgs/{img_id}_processed.png", img_processed)

    return {"old": f"{img_id}.png", 
    "new" : f"{img_id}_processed.png"
    }


@app.post("/files")
async def UploadImage(file: UploadFile = File(...)):
    name = datetime.now().strftime("%Y%m%d-%H%M%S")

    img = await file.read()
    """
    arr = np.asarray(bytearray(img), dtype=np.uint8)
    img = cv.imdecode(arr, -1) # 'Load it as it is'
    img_processed = ImageProcessor(img = img).enhance()
    """
    image_processor = ImageProcessor(img = img)
    img_processed = image_processor.enhance()
    raw_img = image_processor.image
    
    #cv.imwrite(f"{str(parent_path)}/FRONTEND/src/assets/imgs/{str(name)}.png", raw_img)
    #cv.imwrite(f"{str(parent_path)}/FRONTEND/src/assets/processed_imgs/{str(name)}_processed.png", img_processed)

    cv.imwrite(f"{str(parent_path)}/BACKEND/api/assets/imgs/{str(name)}.png", raw_img)
    cv.imwrite(f"{str(parent_path)}/BACKEND/api/assets/processed_imgs/{str(name)}_processed.png", img_processed)

    return {"old": str(name)+".png",
    "new": str(name)+"_processed.png"
    }

@app.post("/enhance")
async def getInformation(info : Request):
    req_info = await info.json()
    img_path=f"{str(parent_path)}/FRONTEND/src/assets/imgs/{req_info[0]['url']}"
    name = datetime.now().strftime("%Y%m%d-%H%M%S")
    img_raw=cv.cvtColor(cv.imread( img_path ) , cv.COLOR_BGR2RGB)
    img_processed=ImageProcessor.processing_pipeline(img = img_raw,jsn= req_info[1]['params'])

    #cv.imwrite(f"{str(parent_path)}/FRONTEND/src/assets/processed_imgs/{name}_processed.png", img_processed)
    
    cv.imwrite(f"{str(parent_path)}/BACKEND/api/assets/processed_imgs/{name}_processed.png", img_processed)

    return {"old": req_info[0]['url'],
    "new": f"{name}_processed.png"
    }