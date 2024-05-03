import json
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from tensorflow.keras.models import load_model
import numpy as np

app = FastAPI()

# Define the input data model
class model_input(BaseModel):
    radius_mean: float
    texture_mean: float
    perimeter_mean: float
    area_mean: float
    smoothness_mean: float
    compactness_mean: float
    concavity_mean: float
    concave_points_mean: float
    symmetry_mean: float
    fractal_dimension_mean: float
    radius_se: float
    texture_se: float
    perimeter_se: float
    area_se: float
    smoothness_se: float
    compactness_se: float
    concavity_se: float
    concave_points_se: float
    symmetry_se: float
    fractal_dimension_se: float
    radius_worst: float
    texture_worst: float
    perimeter_worst: float
    area_worst: float
    smoothness_worst: float
    compactness_worst: float
    concavity_worst: float
    concave_points_worst: float
    symmetry_worst: float
    fractal_dimension_worst: float

# Load the HDF5 model
model_file = 'models\\ysa_model.h5'
model = load_model(model_file) # compile=False

@app.get("/")
async def read_root(request: Request):
    return HTMLResponse(open("pages\mainpage.html", "r").read())

@app.get("/about") 
def about():
    return HTMLResponse(open(r"pages\aboutme.html", "r").read())

@app.get("/prediction")
async def prediction(request: Request):
    return HTMLResponse(open("pages\prediction.html", "r").read())

@app.post("/predict/")
async def predict(input_parameters: model_input):
    input_data = input_parameters.model_dump_json()
    input_dictionary = json.loads(input_data)

    radius_mean = input_dictionary['radius_mean']
    texture_mean = input_dictionary['texture_mean']
    perimeter_mean = input_dictionary['perimeter_mean']
    area_mean = input_dictionary['area_mean']
    smoothness_mean = input_dictionary['smoothness_mean']
    compactness_mean = input_dictionary['compactness_mean']
    concavity_mean = input_dictionary['concavity_mean']
    concave_points_mean = input_dictionary['concave_points_mean']
    symmetry_mean = input_dictionary['symmetry_mean']
    fractal_dimension_mean = input_dictionary['fractal_dimension_mean']
    radius_se = input_dictionary['radius_se']
    texture_se = input_dictionary['texture_se']
    perimeter_se = input_dictionary['perimeter_se']
    area_se = input_dictionary['area_se']
    smoothness_se = input_dictionary['smoothness_se']
    compactness_se = input_dictionary['compactness_se']
    concavity_se = input_dictionary['concavity_se']
    concave_points_se = input_dictionary['concave_points_se']
    symmetry_se = input_dictionary['symmetry_se']
    fractal_dimension_se = input_dictionary['fractal_dimension_se']
    radius_worst = input_dictionary['radius_worst']
    texture_worst = input_dictionary['texture_worst']
    perimeter_worst = input_dictionary['perimeter_worst']
    area_worst = input_dictionary['area_worst']
    smoothness_worst = input_dictionary['smoothness_worst']
    compactness_worst = input_dictionary['compactness_worst']
    concavity_worst = input_dictionary['concavity_worst']
    concave_points_worst = input_dictionary['concave_points_worst']
    symmetry_worst = input_dictionary['symmetry_worst']
    fractal_dimension_worst = input_dictionary['fractal_dimension_worst']

    input_list = [radius_mean, texture_mean, perimeter_mean, area_mean, smoothness_mean, compactness_mean, concavity_mean, concave_points_mean, symmetry_mean, fractal_dimension_mean, radius_se, texture_se, perimeter_se, area_se, smoothness_se, compactness_se, concavity_se, concave_points_se, symmetry_se, fractal_dimension_se, radius_worst, texture_worst, perimeter_worst, area_worst, smoothness_worst, compactness_worst, concavity_worst, concave_points_worst, symmetry_worst, fractal_dimension_worst]

    # # Make prediction
    input_array = np.array(input_list)
    input_array = input_array.reshape(1, -1)
    prediction = model.predict([input_array])

    # Process prediction result
    print("PREDICTION ", prediction)
    if (prediction[0][0]) < 0.5:
        print('The biopsy results revealed benign (B) breast tissue, indicating the absence of cancer.')
        return {'prediction': 'The biopsy results revealed benign (B) breast tissue, indicating the absence of cancer.'}
    else:
        print('The biopsy results revealed malignant (M) breast tissue, indicating the presence of cancer.')
        return {'prediction': 'The biopsy results revealed malignant (M) breast tissue, indicating the presence of cancer.'}