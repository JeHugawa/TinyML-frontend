import json
import random
import os
import requests

from config import BACKEND_URL


def observe_device(device_id,bridge_id):
    
    if os.environ.get("ROBOT_TESTS") == "true":
        target = "%.2f" % random.uniform(0, 100)
        not_target = "%.2f" % random.uniform(0, 100)

    else:
        response = requests.get(f"{BACKEND_URL}/observations/bridges/{bridge_id}/devices/{device_id}", timeout = 2)
        data = json.loads(response.text)
        target = data["observation_value"]["1"]
        not_target = data["observation_value"]["0"]
    
    return {"target": target, "not_target": not_target}

def observe_device_with_dataset_feed(device_id):
    """For demo purposes. This tells the backend to feed images from the
    models dataset to the device. 
    """
    pass
        
