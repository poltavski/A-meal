"""Settings for api service."""
import pickle
import os

if os.environ.get("DOCKER"):
    FOOD_101_CLASSES_PATH = "app/api/networks/food-101/food101_classes.data"
    FOOD_101_MODEL_PATH = "app/api/networks/food-101/model_19.pt"
    MODEL_DIR = "app/api/networks/u2net/u2netp.pth"
    STATIC_FOLDER = "app/api/_static"
    IMAGE_FOLDER = "app/api/images"
else:
    FOOD_101_CLASSES_PATH = "api/networks/food-101/food101_classes.data"
    FOOD_101_MODEL_PATH = "api/networks/food-101/model_19.pt"
    MODEL_DIR = "api/networks/u2net/u2netp.pth"
    STATIC_FOLDER = "api/_static"
    IMAGE_FOLDER = "api/images"

FOOD_101_CLASSES = None
NOT_FOUND_IMAGE = "default.jpg"
INFERENCE_THRESHOLD = 0.5



with open(FOOD_101_CLASSES_PATH, "rb") as filehandle:
    # read the data as binary data stream
    FOOD_101_CLASSES = pickle.load(filehandle)
