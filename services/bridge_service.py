import os
import json
import requests
import pandas as pd


BACKEND_URL = os.getenv("BACKEND_URL")


def add_bridge(address: str, name: str = None):
    data = {
        "ip_address": address,
        "name": name
    }
    data = {key: val if len(val) > 0 else None for key, val in data.items()}
    response = requests.post(f"{BACKEND_URL}/bridges/", json=data, timeout=5)
    if response.status_code == 201:
        return None
    return json.loads(response.text)


def remove_bridge(*args):
    """Removes device from backend based on device_id.

    Args:
        *args: device_id as a tuple
    """

    bridge_id = ''.join(args)
    response = requests.delete(f"{BACKEND_URL}/bridges/{bridge_id}", timeout=5)

    if response.status_code == 400:
        raise ValueError()


def get_registered_bridges():
    """Return a list of all registered devices on backend"""

    response = requests.get(f"{BACKEND_URL}/bridges/", timeout=5)

    if response.text == '[]':
        raise ValueError()
    dataframe = pd.read_json(response.text)

    return dataframe


def try_conntection(address: str):
    if os.environ.get("ROBOT_TESTS") == "true":
        return True
    if "http" not in address:
        address = "http://" + address + ":5000"
    try:
        requests.get(address, timeout=5)
        return True
    except requests.exceptions.ConnectionError:
        return False
