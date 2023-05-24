import pandas as pd
import requests
import os
import json
import pandas as pd

from dotenv import load_dotenv
load_dotenv()

BACKEND_URL = os.getenv("BACKEND_URL")
    

def get_registered_devices():
    response = requests.get(f"{BACKEND_URL}/registered_devices/")
    data = json.loads(response.text)
    df = pd.read_json(data)
    
    if df.empty: 
        return None
    
    return df

def remove(*args):
    device_id = ''.join(args)
    response = requests.delete(f"{BACKEND_URL}/remove_device/{device_id}")
    