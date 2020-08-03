import os
from fastapi import FastAPI
from fastapi import Path
from fastapi.responses import RedirectResponse
from http import HTTPStatus
import json
from pydantic import BaseModel

from image_captioning import config
from image_captioning import utils


app = FastAPI(
    title="image_captioning",
    description="",
    version="1.0.0",
)


@utils.construct_response
@app.get("/")
async def _index():
    response = {
        'message': HTTPStatus.OK.phrase,
        'status-code': HTTPStatus.OK,
        'data': {}
    }
    config.logger.info(json.dumps(response, indent=2))
    return response


class PredictPayload(BaseModel):
    pass


@utils.construct_response
@app.post("/predict")
async def _predict(payload: PredictPayload):
    pass
