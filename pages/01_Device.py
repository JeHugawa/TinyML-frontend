import streamlit as st
import requests

import os
import usb.core
import usb.util
import json
import pandas as pd

from dotenv import load_dotenv

load_dotenv()

BACKEND_URL = os.getenv("BACKEND_URL")  # "http://backend:8000/"
ACCEPTED_VENDORS = ["Raspberry Pi", "Arduino"]

st.set_page_config(
    page_title='Device',
    page_icon='✅',
    layout='wide'
)


def send_add_request():
    state = st.session_state
    data = {
        "name": state.device_name,
        "connection": state.connection,
        "installer": state.installer,
        "compiler": state.compiler,
        "model": state.model,
        "description": state.description
    }
    data = {key: val if len(val) > 0 else None for key, val in data.items()}
    requests.post(f"{BACKEND_URL}/add_device/", json=data)


def handle_add(manufacturer="", product="", serial=""):
    with st.form("new_device"):
        st.write("Add a new device")
        st.text_input("Device name", key="device_name", value=manufacturer)
        st.text_input("Connection", key="connection")
        st.text_input("Installer", key="installer")
        st.text_input("Compiler", key="compiler")
        st.text_input("Model", key="model", value=product)
        st.text_input("Description", key="description")

        col1, col2, col3, col4, col5, col6 = st.columns(6)
        col1.form_submit_button(label='Add', on_click=send_add_request)
        col6.form_submit_button(label='Cancel')


def load_page_info():
    col = st.columns(4)
    col[0].title('Device')
    with col[-1].expander("ℹ️ Help"):
        st.markdown("On this page you can connect to a bridging device.")
        st.markdown(
            "It will eventually also show an overview of connected devices.")
        # Documentation has not been brought to this version yet
        # st.markdown("[See the doc page for more info](/Documentation)")


def list_connected_devices():
    st.header("Connected devices")

    st.button("Refresh", key="refresh")

    devices = list(usb.core.find(find_all=True))

    for device in devices:
        try:
            if usb.util.get_string(device, device.iManufacturer) not in ACCEPTED_VENDORS:
                devices.remove(device)
        except:
            devices.remove(device)
            continue

    col1, col2, col3, col4 = st.columns(4)

    if devices:
        for i, device in enumerate(devices, start=1):
            # Try / Except if any error occurs
            try:
                manufacturer = usb.util.get_string(
                    device, device.iManufacturer)
                product = usb.util.get_string(device, device.iProduct)
                serial = usb.util.get_string(device, device.iSerialNumber)

                if manufacturer is not None:
                    col1.write(manufacturer)
                    col2.write(product)
                    col3.write(serial)
                    col4.button("register this device", key=i, on_click=handle_add, args=(
                        manufacturer, product, serial))
            except Exception as e:
                st.write("Error: " + str(e))
                continue
    else:
        st.write("No devices found")


def registered_devices():
    # List all registered devices
    st.header("All registered devices")
    response = requests.get(f"{BACKEND_URL}/registered_devices/")
    data = json.loads(response.text)
    df = pd.read_json(data)

    # taulukko
    st.table(df)


def main():
    load_page_info()

    list_connected_devices()

    registered_devices()


main()
