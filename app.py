import pickle
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class InputData(BaseModel):
    col1: float
    col2: float
    col3: float
    col4: float
    col5: float
    col6: float
    col7: float
    col8: float
    col9: float

@app.get("/")
def read_root():
    return {"message": "FastAPI ML prediction service is running!"}

@app.post("/predict/")
async def predict_value(input_data: InputData):
    input_list_data = [input_data.col1, input_data.col2, input_data.col3, input_data.col4, input_data.col5, input_data.col6, input_data.col7, input_data.col8, input_data.col9]
    with open('model.pkl', 'rb') as f:
        model = pickle.load(f)
    prediction = model.predict([input_list_data])
    return {"PredictedValue": prediction[0]}