import pandas as pd
import requests
import json

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


def add_new_dataset(dataset_name: str, dataset_desc:str ,files):
    """Adds a new dataset on backend

    Args:
        dataset_name: Name for the new dataset
        dataset_desc: description for the new dataset
        files: Images to initially add to the path. Streamlit UploadedFile class is "filelike" object so we can pass it as is
    """
    data = {
            "dataset_name": dataset_name,
            "dataset_desc": dataset_desc
            }
    dataset_res = requests.post(f"{BACKEND_URL}/datasets/", params=data)
    if dataset_res.status_code != 201:
        return dataset_res.status_code
    dataset_id = dataset_res.json()["id"]
    files_list = []
    for file in files:
        files_list.append(('files', file))
    addimg_res = requests.post(f"{BACKEND_URL}/datasets/{dataset_id}/", files=files_list)
    return addimg_res.status_code
