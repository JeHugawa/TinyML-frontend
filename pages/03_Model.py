import streamlit as st
from datetime import datetime
from pages.sidebar import sidebar
from services import model_service

state = st.session_state

st.set_page_config(
    page_title="Model",
    layout="wide"
)

sidebar.load_side_bar()


def load_page_info():
    st.header("Available machine learning models")


def list_trained_models():
    models = model_service.get_models()

    col = st.columns(11)
    col[0].write("ID")
    col[1].write("Description")
    col[2].write("Epochs")
    col[3].write("Batch size")
    col[4].write("Dataset")
    col[5].write("Created")
    for model in models:
        dataset_id, parameters, description, id, created, _ = model.values()
        created = datetime.fromisoformat(created)
        created = created.strftime("%d/%m/%Y %H:%M")
        col[0].write(id)
        col[1].write(description)
        col[2].write(parameters["epochs"])
        col[3].write(parameters["batch_size"])
        col[4].write(dataset_id)
        col[5].write(created)


def main():
    load_page_info()

    list_trained_models()


main()
