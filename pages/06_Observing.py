import time
import streamlit as st

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
        st.markdown(
            "On this page you can observe the predictions sent from the TinyML device.")
        st.markdown(
            "Click the Start button to start reading predictions from the device")


def observe_person_detection():
    good_to_go = "bridge" in state and "device" in state

    if not good_to_go:
        if "bridge" not in st.session_state:
            st.error("Bridge not selected. Please select it on the device page.")

        if "device" not in st.session_state:
            st.error("Select device to observe.")

    else:

        bt_columns = st.columns(8)
        start_clicked = bt_columns[0].button("Start")
        stop_clicked = bt_columns[1].button("Stop")

        prediction_target = st.empty()
        prediction_not_target = st.empty()

        while start_clicked and not stop_clicked:
            for i in range(0, 10):
                time.sleep(0.5)
                prediction = observing_service.observe_device(
                    state.device['id'], state.bridge['id'])
                # st.write(prediction)
                prediction_target.write(
                    f"Image is target: {prediction['target']}%")
                prediction_not_target.write(
                    f"Image is not target: {prediction['not_target']}%")


def main():
    sidebar.load_side_bar()
    page_info()
    observe_person_detection()


main()
