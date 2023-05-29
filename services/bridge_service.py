import requests
import os
import json
import pandas as pd


BACKEND_URL = os.getenv("BACKEND_URL")


def add_bridge(address: str, name: str = None):
    data = {
        "ip_address": address,
        "name": name
    }
    data = {key: val if len(val) > 0 else None for key, val in data.items()}
    response = requests.post(f"{BACKEND_URL}/add_bridge/", json=data)
    if response == 201:
        return None
    return json.loads(response.text)


def get_registered_bridges():
    res = requests.get(f"{BACKEND_URL}/registered_bridges/")
    data = json.loads(res.text)
    df = pd.read_json(data)

    return df


def try_conntection(address: str):
    if "http" not in address:
        address = "http://" + address
    try:
        requests.get(address)
        return True
    except requests.exceptions.ConnectionError:
        return False