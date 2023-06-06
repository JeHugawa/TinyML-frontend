import os
import json
import base64
import requests


BACKEND_URL = os.getenv("BACKEND_URL")


def train_model(dataset_id: int, model_name: str, parameters: dict, lossfunc: str):
    data = {
        "dataset_id": dataset_id,
        "parameters": parameters,
        "description": model_name
    }
    response = requests.post(f"{BACKEND_URL}/model/dataset/?lossfunc={lossfunc}",
                             json=data, timeout=(5, None))
    if response.status_code == 201:
        res = response.text.strip('][').split(', ')
        response_dict = json.loads(res[0])
        img_pred = base64.b64decode(response_dict["prediction_image"])
        img_stats = base64.b64decode(response_dict["statistic_image"])
        return [img_pred, img_stats, response_dict]
    return json.loads(response.text)
