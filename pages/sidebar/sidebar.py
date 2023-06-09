import streamlit as st

state = st.session_state

def load_side_bar():
    if "bridge" in state:
        st.sidebar.write(f"Selected bridge: :green[{state.bridge}]")
    if "device" in state:
        st.sidebar.write(
            f"Selected device: :green[{state.device['device_name']}]")
        st.sidebar.write(
            f"Description: :orange[{state.device['description']}]")
    if "dataset" in state:
        st.sidebar.write(
            f"Selected dataset: :green[{state.dataset['name']}]"
        )
    if "model" in state:
        st.sidebar.write(
            f"Selected model: :green[{state.model['description']}]")
