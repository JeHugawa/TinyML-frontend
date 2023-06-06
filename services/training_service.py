import os
import json
import base64
import requests
import pandas as pd


BACKEND_URL = os.getenv("BACKEND_URL")


def train_model(dataset_id: int, model_name: str, epochs: int,
                img_width: int, img_height: int, batch_size: int, lossfunc: str):
    data = {
        "model_name": model_name,
        "epochs": epochs,
        "img_width": img_width,
        "img_height": img_height,
        "batch_size": batch_size
    }
    response = requests.post(f"{BACKEND_URL}/model/dataset/{dataset_id}?lossfunc={lossfunc}",
                             json=data, timeout=(5, None))
    res = response.text.strip('][').split(', ')
    response_dict = json.loads(res[0])
    img = base64.b64decode(response_dict["image"])
    if response.status_code == 201:
        return None
    return json.loads(response.text)
