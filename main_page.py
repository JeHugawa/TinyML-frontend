import streamlit as st
import requests
import os
import json

st.markdown('# Pääsivu')
st.sidebar.markdown("# Pääsivu")

BACKEND_URL = os.getenv("BACKEND_URL")

data = requests.get(f"{BACKEND_URL}/dataset_names/")
datasets = json.loads(data.text)
data = requests.get(f"{BACKEND_URL}/registered_devices/")
devices = json.loads(data.text)


st.write(devices.count("id"), " Devices registered")
st.write(len(datasets["dataset_names"]), " Datasets saved")
