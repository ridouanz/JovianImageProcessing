from tkinter import Image
from typing import Union
import cv2 as cv
from fastapi import FastAPI
import pathlib
import os
import sys
from fastapi.middleware.cors import CORSMiddleware

parent_path = pathlib.Path(os.path.realpath(__file__)).parent.parent
sys.path.append(str(parent_path))

from src import ImageLoader, ImageProcessor

parent_path = pathlib.Path(os.path.realpath(__file__)).parent.parent.parent
sys.path.append(str(parent_path))
app = FastAPI()

#fix the Cross-Origin Resource Sharing with angular
origins = [
    "http://localhost:4200",
    "http://localhost",
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
    return {"Hello": "World"}


@app.get("/process/{img_id}")
def read_item(img_id : str):
    img_raw = ImageLoader(img_id).load()
    img_processed = ImageProcessor(img_id).enhance()
    ##cv.imwrite(f"{str(parent_path)}/data/raw/{img_id}.png", img_raw)
    ##cv.imwrite(f"{str(parent_path)}/data/processed/{img_id}.png", img_processed)

    cv.imwrite(f"{str(parent_path)}/FRONTEND/src/assets/dataProcess/{img_id}_edited.png", img_processed)
    return {"img": f"{img_id}_edited.png"}