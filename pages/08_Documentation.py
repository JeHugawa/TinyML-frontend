import streamlit as st
import os
from dotenv import load_dotenv
load_dotenv()

BACKEND_URL = os.getenv("BACKEND_URL")

st.set_page_config(
    page_title="Observing", 
    layout="wide"
    )

st.header("Documentation")
link_github = "[GitHub](https://github.com/TinyMLaas)"
link_pages = "[Project presentation](https://origami-tinyml.github.io/tflm_hello_world/)"
link_backend_docs = f"[Backend API documentation]({BACKEND_URL}/docs)"

st.markdown(link_github, unsafe_allow_html=True)
st.markdown(link_pages, unsafe_allow_html=True)
st.markdown(link_backend_docs, unsafe_allow_html=True)