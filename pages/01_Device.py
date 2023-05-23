import streamlit as st 
import requests
import os
import json
import pandas as pd

from dotenv import load_dotenv
load_dotenv()

BACKEND_URL = os.getenv("BACKEND_URL")

st.set_page_config(
    page_title='Device',
    page_icon='✅',
    layout='wide'
)

# List all registered devices
st.header("All registered devices")
response = requests.get(f"{BACKEND_URL}/registered_devices/")
data = json.loads(response.text)
df = pd.read_json(data)

# taulukko
st.table(df)

