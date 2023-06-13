import time
from datetime import datetime
import streamlit as st
import pandas as pd

from pages.sidebar import sidebar
from services import observing_service

st.set_page_config(
    page_title="Observing",
    layout="wide"
)

state = st.session_state

def page_info():
    col = st.columns(4)

    with col[-1].expander("ℹ️ Help"):
        st.markdown("On this page you can observe the predictions sent from the TinyML device.")
        st.markdown("Click the Start button to start reading predictions from the device")


def observe_person_detection():
    good_to_go = "bridge" in state and "device" in state

    if not good_to_go:
        if "bridge" not in st.session_state:
            st.error("Bridge not selected. Please select it on the device page.")


        if "device" not in st.session_state:
            st.error("Select device to observe.")
            st.write("<LIST OF DEVICES CONNECTED TO THIS BRIDGE>")

    else:

        bt_columns = st.columns(8)
        start_clicked = bt_columns[0].button("Start")
        stop_clicked = bt_columns[1].button("Stop")

        predictions = st.empty()

        while start_clicked and not stop_clicked:
            for i in range(0,10):
                time.sleep(0.5)
                prediction = observing_service.observe_device(1)
                predictions.write(f"Prediction score: {prediction}")


def main():
    sidebar.load_side_bar()
    page_info()
    observe_person_detection()

main()