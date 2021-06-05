"""Settings for api service."""
import pickle

FOOD_101_CLASSES_PATH = "../models/food-101/food101_classes.data"
FOOD_101_MODEL_PATH = "../models/food-101/model_19.pt"
FOOD_101_CLASSES = None

with open(FOOD_101_CLASSES_PATH, "rb") as filehandle:
    # read the data as binary data stream
    FOOD_101_CLASSES = pickle.load(filehandle)
