import streamlit as st

from pages.sidebar import sidebar

# from config import BACKEND_URL

APIDOCSURL = "https://tiny.marenk.fi/api/docs"

st.set_page_config(
    page_title="Documentation",
    layout="wide"
)

sidebar.load_side_bar()

st.header("Documentation")
LINK_GITHUB = "[GitHub](https://github.com/TinyMLaas)"
LINK_PAGES = "[Project presentation](https://tinymlaas.github.io/TinyMLaaS/)"
LINK_BACKEND_DOCS = f"[Backend API documentation]({APIDOCSURL})"

st.markdown(LINK_GITHUB, unsafe_allow_html=True)
st.markdown(LINK_PAGES, unsafe_allow_html=True)
st.markdown(LINK_BACKEND_DOCS, unsafe_allow_html=True)
