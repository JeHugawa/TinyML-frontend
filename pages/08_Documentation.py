import streamlit as st

st.set_page_config(
    page_title="Observing", 
    layout="wide"
    )

st.header("Documentation")
link_github = '[GitHub](https://github.com/TinyMLaas)'
link_pages = '[Project presentation](https://origami-tinyml.github.io/tflm_hello_world/)'

st.markdown(link_github, unsafe_allow_html=True)
st.markdown(link_pages, unsafe_allow_html=True)