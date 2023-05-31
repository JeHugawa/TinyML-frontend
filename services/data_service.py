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
    if dataset == {}:
        return ""
    return dataset["name"] + " size: " + dataset["size"]

def add_image_to_dataset(dataset,image):
    response = requests.put(f"{BACKEND_URL}/add_image",data=image)
    if response.status_code == 201:
        return "Success"
    if response.status_code == 404:
        return "Not implemented"
