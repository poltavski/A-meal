from fastapi import FastAPI, File, HTTPException
from PIL import Image
from io import BytesIO

# import numpy as np
import logging
import requests
import sys
import uvicorn
from fastapi.staticfiles import StaticFiles

# from fastapi.responses import FileResponse
# from utils import (
# process_image,
# process_plate_image,
# visualize_results,
# CarRecognition,
# PlateRecognition,
# LetterRecognition,
# BrandRecognition,
# ColorRecognition,
# DirectionRecognition,
# )
# from cv2 import cvtColor, imwrite, COLOR_RGB2BGR
from fastapi.middleware.cors import CORSMiddleware

sys.setrecursionlimit(1500)
logging.basicConfig(
    filename="server.log",
    level=logging.DEBUG,
    filemode="a",
    format="%(asctime)s: %(funcName)s - %(levelname)s - %(message)s",
)

app = FastAPI()
app.mount("/_static", StaticFiles(directory="_static"), name="_static")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# car_detector = CarRecognition()
# plate_detector = PlateRecognition()
# letter_detector = LetterRecognition()
# brand_classifier = BrandRecognition()
# color_classifier = ColorRecognition()
# direction_classifier = DirectionRecognition()


def analyse(image: Image):
    """Perform inference on image.

    Args:
        image: Image,
            provided image

    Returns:
        dict of recognized properties of vehicle items.
    """
    pass


@app.get("/")
async def main():
    """
    ping method for api call
    Returns:
        200
    """
    return


@app.get("/inference/static")
def inference_static(image_name: str = "example1.jpg"):
    """
    get binary images method for api call
    Returns:

    """
    try:
        image = Image.open(f"_static/{image_name}", mode="r").convert("RGB")
    except:
        raise HTTPException(
            500, detail={"status": f"{image_name} not found in static files on server"}
        )
    try:
        result = analyse(image)
    except:
        raise HTTPException(500, detail={"status": f"Analysis failed on {image_name}"})
    if result:
        return {"result": result, "status": 0}
    else:
        raise HTTPException(
            422, detail={"status": f"{image_name} returned empty results"}
        )


@app.get("/inference/demo")
async def inference_demo(
    url: str = "https://nsa39.casimages.com/img/2018/09/12/180912122808840707.jpg",
):
    """
    Public endpoint for demo fashion analysis by GET request

    Args:
        url: image url

    Returns:
        jpg image with recognized vehicle items
    """
    response = requests.get(url)
    image = Image.open(BytesIO(response.content)).convert("RGB")
    result = analyse(image)
    if result:
        pass
        # result_image = visualize_results(image, result)
        # imwrite("result.jpg", cvtColor(result_image, COLOR_RGB2BGR))
        # return FileResponse("result.jpg")


@app.get("/inference/url")
async def inference_url(
    url: str = "https://nsa39.casimages.com/img/2018/09/12/180912122808840707.jpg",
):
    """
    Public endpoint for vehicle analysis by GET request
    Args:
        url: image url

    Returns:
        json string of results
    """
    response = requests.get(url)
    img = Image.open(BytesIO(response.content)).convert("RGB")
    result = analyse(img)
    print(result)
    if result:
        return {"result": result, "status": 0}
    else:
        return {"result": "Given image returned empty results", "status": 1}


@app.post("/inference/file")
async def inference_file(file: bytes = File(...)):
    """
    Handles image file path and urls

    Args:
        file: file in binary formatnetstat -tulpen

    Returns:
        json string of results
    """
    img = Image.open(BytesIO(file)).convert("RGB")
    result = analyse(img)
    if result:
        return {"result": result, "status": 0}
    else:
        return {"result": "Given image returned empty results", "status": 1}


if __name__ == "__main__":
    uvicorn.run("server:app", host="0.0.0.0", port=8050, log_level="info")
