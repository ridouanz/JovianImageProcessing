from tkinter import Image
from typing import Union
import cv2 as cv
from fastapi import FastAPI
import pathlib
import os
import sys

parent_path = pathlib.Path(os.path.realpath(__file__)).parent.parent
print('--------------------', parent_path)
sys.path.append(str(parent_path))
from src import ImageLoader

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/process/{img_link}")
def read_item(img_link : str):
    img = ImageLoader(img_link).load()
    img_processed = img[:,:,1] + 50
    cv.imwrite(f"{str(parent_path)}/data/img.png", img_processed)
    
    return {"img": f"{str(parent_path)}/data/img.png"}