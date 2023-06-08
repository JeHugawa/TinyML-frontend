import json
import requests

from config import BACKEND_URL


def get_models():
    response = requests.get(f"{BACKEND_URL}/models/", timeout=5)
    if response.status_code == 200:
        return json.loads(response.text)
    return None
