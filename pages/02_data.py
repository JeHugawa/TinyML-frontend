import streamlit as st
import requests
import os
import json
import pandas as pd

from dotenv import load_dotenv

load_dotenv()

BACKEND_URL = os.getenv("BACKEND_URL")

st.set_page_config(page_title="Device", page_icon="✅", layout="wide")

# List all registered devices
st.header("Existing datasets")
response = requests.get(f"{BACKEND_URL}/dataset_names/")
data = json.loads(response.text)

# taulukko
st.table(data)

st.header('Data')
st.write('Select a dataset')

def format_datasets(dataset):
    return dataset["name"] + " size: " + dataset["size"]

if 'selected_dataset' not in st.session_state:
    st.session_state['selected_dataset'] = None
    
response = requests.get(f"{BACKEND_URL}/dataset_names_size/")
data = json.loads(response.text)
st.session_state['selected_dataset'] = st.selectbox('Select a dataset: ', data, format_func=format_datasets)
st.write('You selected:', st.session_state['selected_dataset'])

