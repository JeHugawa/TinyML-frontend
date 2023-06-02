import pandas as pd
import requests
import os
import json
import pandas as pd

from config import BACKEND_URL    


def get_saved_datasets():
    """Return a list of all registered devices on backend"""
    
    response = requests.get(f"{BACKEND_URL}/datasets/")

    if response.text == []:
        raise ValueError()
    else:
        df = pd.read_json(response.text)

    return df


def get_no_of_datasets():
    df = get_saved_datasets()
    
    return df.shape[0]


def format_datasets(dataset):
    return dataset["name"]