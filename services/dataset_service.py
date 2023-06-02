import pandas as pd
import requests

#import pandas as pd

from config import BACKEND_URL


def get_saved_datasets():
    """Return a list of all registered devices on backend"""

    response = requests.get(f"{BACKEND_URL}/datasets/", timeout=5)

    if response.text == []:
        raise ValueError()

    datasets = pd.read_json(response.text)

    return datasets


def get_no_of_datasets():
    datasets = pd.DataFrame(get_saved_datasets())
    return datasets.shape[0]


def format_datasets(dataset):
    return dataset["name"]
