import json
import requests

from config import BACKEND_URL


def get_dataset_names():
    response = requests.get(f"{BACKEND_URL}/dataset_names/", timeout=5)
    data = json.loads(response.text)
    return data


def get_dataset_names_size():
    response = requests.get(f"{BACKEND_URL}/dataset_names_size/", timeout=5)
    data = json.loads(response.text)
    return data


def format_datasets(dataset):
    return dataset["name"] + " size: " + dataset["size"]
