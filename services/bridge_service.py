import requests
import os
import json

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
