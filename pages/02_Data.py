import streamlit as st

from pages.sidebar import sidebar
from services import dataset_service


st.set_page_config(
    page_title="Data",
    page_icon="✅",
    layout="wide"
)

sidebar.load_side_bar()

state = st.session_state


def select_dataset(*args):
    state.dataset_id = args[0]
    state.dataset_name = args[1]
    state.dataset_description = args[2]
    state.dataset_size = args[3]
    st.success(f"You have selected **{state.dataset_name}** dataset.")


st.header("Existing datasets")


def load_side_bar():
    if "bridge" in state:
        st.sidebar.write(f"Selected bridge: :green[{state.bridge}]")
    if "device" in state:
        st.sidebar.write(f"Selected device: :green[{state.device['id']}]")
        st.sidebar.write(
            f"Description: :orange[{state.device['description']}]")


try:
    existing_datasets = dataset_service.get_saved_datasets()

    col1, col2, col3, col4 = st.columns(4)

    col = st.columns(10)
    col[0].write("Id")
    col[1].write("Name")
    col[2].write("Description")
    col[3].write("Size")
    for row in existing_datasets.sort_values("id").itertuples():
        index, path, name, description, size, id = row
        col = st.columns(11)
        col[0].write(id)
        col[1].write(name)
        col[2].write(description)
        col[3].write(size)
        col[4].button("Select", key=f"s_{id}_{name}", on_click=select_dataset, args=(
            id, name, description, size))

except:
    st.warning("No datasets available.")
