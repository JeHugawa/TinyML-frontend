import streamlit as st
import pandas as pd

from services import data_service, device_service

# Page setup
st.set_page_config(
    page_title="TinyMLaaS",
    layout="wide"
)
st.title("Welcome to TinyMLaaS")

st.header("Device Location Map")
device_locations = pd.DataFrame({
    "device_id": ["Arduino 1", "Arduino 2", "Raspberry pi 2", "undefined device"],
    "latitude": [60.203978, 60.208609, 60.207861, 60.201926],
    "longitude": [24.961129, 24.966743, 24.965956, 24.968977],
    "last_update": [
        "2022-03-01 12:30:00",
        "2022-03-01 14:45:00",
        "2022-03-01 13:00:00",
        "2022-03-01 11:00:00"
    ]
})

st.map(device_locations[["latitude", "longitude"]], zoom=13)

st.header("Statistical Data")

datasets = data_service.get_dataset_names()

devices = device_service.get_registered_devices()

st.write(len(devices), "Devices registered")
st.write(len(datasets["dataset_names"]), " Datasets saved")
