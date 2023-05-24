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
    
    return df

def show_registered_devices():
    pass