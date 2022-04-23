import uvicorn
from fastapi import FastAPI 

import joblib,os

model_file = open("/app/model/model_joblib","rb")
model_condo = joblib.load(model_file)

#init app
app = FastAPI()

#Routes
@app.get('/')
async def index():
    return {"text": "Hello API Builders"}

@app.get('/items/{name}')
async def get_items(name):
    return {"name":name}

@app.get('/predict/{sqft}')
async def predict(sqft):
    result = model_condo.predict([[sqft]])
    return result[0]

if __name__ == '__main__':
    uvicorn.run(app,host="127.0.0.1",port=80)

