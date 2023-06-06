import requests
import pandas as pd

from config import BACKEND_URL


def compile_model(data: dict):
    """Sends request to backend for compilation. The request uses the model id.
    """
    model_id = data["model_id"]

    response = requests.post(f"{BACKEND_URL}/compiled_models/models/{model_id}", json=data, timeout=5)

    return(f"{data} gets response {response.text}")


def get_compiled_models():
    """Return a list of all compiled models."""
    return ("This is list.")
    # response = requests.get(f"{BACKEND_URL}/compiled_models/", timeout=5)

    # if response.text == []:
    #     raise ValueError()
    # compiled_models = pd.read_json(response.text)

    # return compiled_models
    