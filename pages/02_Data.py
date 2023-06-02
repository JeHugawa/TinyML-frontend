import streamlit as st
from services import data_service

st.set_page_config(
    page_title="Data",
    layout="wide"
)

# List all registered devices
st.header("Existing datasets")
name_data = data_service.get_dataset_names()
st.table(name_data)

st.header("Data")

if "selected_dataset" not in st.session_state:
    st.session_state["selected_dataset"] = None

data = data_service.get_dataset_names_size()
st.session_state["selected_dataset"] = st.selectbox(
    "Select a dataset: ", data, format_func=data_service.format_datasets)

st.success(
    (f"You selected: {st.session_state['selected_dataset']['name']} dataset,"
     f"size {st.session_state['selected_dataset']['size']}"))
