from fastapi import FastAPI
from pydantic import BaseModel
from models.model_loader import predict_anxiety

app = FastAPI()

class TextInput(BaseModel):
    text: str

@app.get("/")
def home():
    return {"message": "AI Exam Anxiety Detector API"}

@app.post("/predict")
def predict(data: TextInput):

    result = predict_anxiety(data.text)

    return {"prediction": result}