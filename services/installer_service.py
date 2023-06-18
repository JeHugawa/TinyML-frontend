import os
import json
import requests

from config import BACKEND_URL


def get_installers():
    """Return a list of all registered / allowed installers"""

    response = requests.get(f"{BACKEND_URL}/installers/", timeout=5)

    if response.text == '[]':
        raise ValueError()
    devices = json.loads(response.text)

    return devices


def send_bridge_install(bridge_id, device_id, compiled_model_id):
    if os.environ.get("ROBOT_TESTS") == "true":
        return True
    res = requests.post(
        f'{BACKEND_URL}/compiled_models/{compiled_model_id}/bridges/{bridge_id}/devices/{device_id}',
        timeout=(5, None))
    if res.status_code != 201:
        return False
    return True
