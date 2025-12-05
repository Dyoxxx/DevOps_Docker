from fastapi import FastAPI
from pymongo import MongoClient
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
import joblib
import numpy as np

model = joblib.load("model.pkl")

class Item(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float
    
app = FastAPI()
client = MongoClient('mongo', 27017)
db = client.test_database
collection = db.test_collection

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/add/{fruit}")
async def add_fruit(fruit: str):
    id = collection.insert_one({"fruit": fruit}).inserted_id 
    return {"id": str(id)}

@app.get("/list")
async def list_fruits():
    return {"results": list(collection.find({}, {"_id": False}))}

class_names = ["setosa", "versicolor", "virginica"]

@app.post("/predict")
def predict(item: Item):
    item_data = jsonable_encoder(item)

    features = np.array([[
        item_data["sepal_length"],
        item_data["sepal_width"],
        item_data["petal_length"],
        item_data["petal_width"]
    ]])

    prediction_idx = model.predict(features)[0]
    prediction_label = class_names[prediction_idx]

    return {
        "input": item_data,
        "prediction": prediction_label
    }
