import cv2 as cv
from fastapi import FastAPI
import pathlib
import os
import sys
from fastapi.middleware.cors import CORSMiddleware

from fastapi import FastAPI, File, Request
from datetime import datetime


parent_path = pathlib.Path(os.path.realpath(__file__)).parent.parent
sys.path.append(str(parent_path))

from src import ImageLoader, ImageProcessor

parent_path = pathlib.Path(os.path.realpath(__file__)).parent.parent.parent
sys.path.append(str(parent_path))
app = FastAPI()

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

@app.get("/")
def read_root():
    return {"msg": "Hello :)"}


@app.post("/process")
async def getInformation(info : Request):
    req_info = await info.json()
    img_id=req_info["img"]
    
    img_raw = ImageLoader(img_id).load()
    img_processed = ImageProcessor(img_id).enhance()

    cv.imwrite(f"{str(parent_path)}/FRONTEND/src/assets/imgs/{img_id}.png", img_raw)
    cv.imwrite(f"{str(parent_path)}/FRONTEND/src/assets/processed_imgs/{img_id}.png", img_processed)

    return {"old": f"{img_id}.png", 
    "new" : f"{img_id}_Processed.png"
    }


@app.post("/files")
async def UploadImage(file: bytes = File(...)):

    timestr = datetime.now().strftime("%Y%m%d-%H%M%S")
    name=timestr+".png"

    with open(f"{str(parent_path)}/FRONTEND/src/assets/imgs/"+str(name),'wb') as image:
        image.write(file)
        image.close()

    ##uploaded_processed= ImageProcessor("the path to the picture").enhance()
    ##cv.imwrite(f"{str(parent_path)}/FRONTEND/src/assets/processed_imgs/{str(name)}", uploaded_processed)

    return {"old": str(name),
    "new": str(name)
    }