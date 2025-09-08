from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
from PIL import Image
import io

from fracture_detector import FractureDetector  
app = FastAPI(title="Fracture Detection API")

detector = FractureDetector("Model.pkl")


def read_image(file: UploadFile) -> Image.Image:
    """Read uploaded file into PIL Image"""
    contents = file.file.read()
    return Image.open(io.BytesIO(contents))


@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    img = read_image(file)
    category = detector.predict(img)
    return JSONResponse({"prediction": category})


@app.post("/has-fracture")
async def has_fracture(file: UploadFile = File(...)):
    img = read_image(file)
    result = detector.hasFracture(img)
    return JSONResponse({"has_fracture": result})


@app.post("/fracture-type")
async def fracture_type(file: UploadFile = File(...)):
    img = read_image(file)
    result = detector.fractureType(img)
    return JSONResponse({"fracture_type": result})