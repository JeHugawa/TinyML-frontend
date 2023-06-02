import streamlit as st
from config import BACKEND_URL

st.set_page_config(
    page_title="Observing",
    layout="wide"
)

st.header("Documentation")
LINK_GITHUB = "[GitHub](https://github.com/TinyMLaas)"
LINK_PAGES = "[Project presentation](https://origami-tinyml.github.io/tflm_hello_world/)"
LINK_BACKEND_DOCS = f"[Backend API documentation]({BACKEND_URL}/docs)"

st.markdown(LINK_GITHUB, unsafe_allow_html=True)
st.markdown(LINK_PAGES, unsafe_allow_html=True)
st.markdown(LINK_BACKEND_DOCS, unsafe_allow_html=True)
