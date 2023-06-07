import streamlit as st

from pages.sidebar import sidebar

state = st.session_state

st.set_page_config(
    page_title="Training",
    layout="wide"
)


st.header("Model Training Camp")

sidebar.load_side_bar()
