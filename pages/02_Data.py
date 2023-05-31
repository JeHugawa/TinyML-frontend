import streamlit as st
import json
from services import data_service


st.set_page_config(
    page_title="Data", 
    page_icon="✅", 
    layout="wide"
    )

def list_all_datasets():
    st.header("Existing datasets")
    name_data = data_service.get_dataset_names()
    st.table(name_data)

def select_dataset():
    data = data_service.get_dataset_names_size()
    st.session_state['selected_dataset'] = st.selectbox('Select a dataset: ', [dict()]+data, format_func=data_service.format_datasets)
    if st.session_state["selected_dataset"]:
        st.write('You selected:', st.session_state['selected_dataset'])
    else:   
        st.write("No dataset selected")

def add_image_to_dataset():
    if st.session_state["selected_dataset"]:
        st.header("Add image to dataset")
        uploaded_file = st.file_uploader("Choose a file")
        if uploaded_file is not None:
            st.warning(data_service.add_image_to_dataset(st.session_state["selected_dataset"],json.dumps(dict())))


def main():
    st.header("Data")
    list_all_datasets()
    select_dataset()
    add_image_to_dataset()

main()


