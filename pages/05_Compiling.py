import streamlit as st

from pages.sidebar import sidebar

state = st.session_state

st.set_page_config(
    page_title="Compiling",
    layout="wide"
)

sidebar.load_side_bar()

st.header("Model compilation makes them tiny")
