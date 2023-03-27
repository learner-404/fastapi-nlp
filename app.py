import uvicorn
from fastapi import FastAPI
from promptgens import promptgen
# import nltkmodules
import numpy as np
import pandas as pd
# import pickle
from writers import writer

app = FastAPI()

@app.get('/')
def index():
    return {'message': 'Hello, World'}

@app.get('/{name}')
def get_name(name: str):
    return {'Welcome ': f'{name}'}


@app.post('/prompt')
# writer(sentence)
def promptgenn(data:promptgen):
    data = data.dict()
    sentence = data['sentence']
    # print(writer(sentence))
    prediction = writer(sentence)
    return {
        'prediction': prediction
    }

# 5. Run the API with uvicorn
#    Will run on http://127.0.0.1:8000
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
    
#uvicorn app:app --reload
