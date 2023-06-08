import streamlit as st

from pages.sidebar import sidebar

state = st.session_state

st.set_page_config(
    page_title="Model",
    layout="wide"
)

sidebar.load_side_bar()

st.header("Available machine learning models")
