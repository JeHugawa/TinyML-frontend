import random
import os
import requests

from config import BACKEND_URL


def observe_device(device_id):
    
    if os.environ.get("ROBOT_TESTS") == "true":
        return("%.2f" % random.uniform(0, 1))

    response = requests.GET(f"{BACKEND_URL}/bridges/ /devices/{device_id}", timeout = 2).json()
    return(response['observation_value'])


def observe_device_with_dataset_feed(device_id):
    """For demo purposes. This tells the backend to feed images from the
    models dataset to the device. 
    """
    pass
        
