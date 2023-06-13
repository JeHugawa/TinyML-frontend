import streamlit as st

from pages.sidebar import sidebar

st.set_page_config(
    page_title="Installing",
    layout="wide"
)

sidebar.load_side_bar()

state = st.session_state

st.header("Install model to MCU")


def install():
    pass


def load_info():
    st.write("Install the selected model to the selected device")
    st.button("Install", on_click=install)


def main():
    load_info()


main()
