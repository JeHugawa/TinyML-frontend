import streamlit as st

from services import bridge_service
from pages.sidebar import sidebar

st.set_page_config(
    page_title="Installing",
    layout="wide"
)

sidebar.load_side_bar()

state = st.session_state

st.header("Install model to MCU")


def install():
    if bridge_service.send_bridge_install(
            state.bridge, state.device, state.compiled_model):
        st.success("Model has been installed successfully to device")
    else:
        st.error("An error has occured while installing the model")


def load_info():
    errors = False
    if "compiled_model" not in state:
        st.error("Please select a compiled model")
        errors = True
    if "bridge" not in state:
        st.error("Please select a bridge")
        errors = True
    if "device" not in state:
        st.error("Please select a device")
        errors = True
    if errors:
        return
    st.write("Install the selected model to the selected device")
    st.button("Install", on_click=install)


def main():
    load_info()


main()
