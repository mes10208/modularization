from typing import List

from fastapi import FastAPI, Query

from src.models.train import train
from src.models.predict import predict

app = FastAPI()


@app.get('/')
async def test():
    return {'return':'hello wolrd'}