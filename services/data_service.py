import pandas as pd
import requests
import os
import json
import pandas as pd

from config import BACKEND_URL    

def get_dataset_names():
    response = requests.get(f"{BACKEND_URL}/dataset_names/")
    data = json.loads(response.text)
    return data


def get_dataset_names_size():
    response = requests.get(f"{BACKEND_URL}/dataset_names_size/")
    data = json.loads(response.text)
    return data


def format_datasets(dataset):
    return dataset["name"] + " size: " + dataset["size"]
