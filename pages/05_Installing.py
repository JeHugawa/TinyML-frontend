import streamlit as st

from pages.sidebar import sidebar

st.set_page_config(
    page_title="Installing",
    layout="wide"
)

sidebar.load_side_bar()

st.header("Install model to MCU")
