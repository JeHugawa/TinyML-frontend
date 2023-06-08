import streamlit as st
from services import dataset_service


st.set_page_config(
    page_title="Data",
    page_icon="✅",
    layout="wide"
)

state = st.session_state

def select_dataset(*args):
    state.dataset_id = args[0]
    state.dataset_name = args[1]
    state.dataset_description = args[2]
    state.dataset_size = args[3]
    st.success(f"You have selected **{state.dataset_name}** dataset.")


st.header("Existing datasets")

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

st.divider()
st.header("Add new dataset")

with st.form("Add a new Dataset"):
    state.add_button = False
    new_dataset_name = st.text_input("Dataset name")
    new_dataset_desc = st.text_input("Description for dataset (optional)")
    st.warning("Uploaded files aren't saved to the server")
    uploaded_files = st.file_uploader("Choose image files", accept_multiple_files=True)
    submitted = st.form_submit_button("Add")
    if submitted:
        response = dataset_service.add_new_dataset(new_dataset_name, new_dataset_desc,uploaded_files) 
        if response == 201:
            st.success("New dataset added")
        else:
            st.error(response)
