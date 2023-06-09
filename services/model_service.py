import json
import base64
import requests

from config import BACKEND_URL


def get_models():
    response = requests.get(f"{BACKEND_URL}/models/", timeout=5)
    if response.status_code == 200:
        return json.loads(response.text)
    return None


def train_model(dataset_id: int, model_name: str, parameters: dict, lossfunc: str):
    data = {
        "dataset_id": dataset_id,
        "parameters": parameters,
        "description": model_name
    }
    response = requests.post(f"{BACKEND_URL}/models/datasets/?lossfunc={lossfunc}",
                             json=data, timeout=(5, None))
    if response.status_code == 201:
        response_dict = json.loads(response.text)
        img_pred = base64.b64decode(response_dict["prediction_image"])
        del response_dict["prediction_image"]
        img_stats = base64.b64decode(response_dict["statistic_image"])
        del response_dict["statistic_image"]
        return [img_pred, img_stats, response_dict]
    return json.loads(response.text)
