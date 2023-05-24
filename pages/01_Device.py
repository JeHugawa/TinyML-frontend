import streamlit as st 

from services import device_service

# Page setup
st.set_page_config(
    page_title='Device',
    page_icon='✅',
    layout='wide'
)

state = st.session_state

# List all registered devices
st.header("All registered devices")

registered_devices = device_service.get_registered_devices()

col1, col2, col3, col4, col5, col6, col7, col8 = st.columns(8)

for row in registered_devices.sort_values("id").itertuples():
    index, id, name, connection, installer, compiler, model, description = row
    col = st.columns(10)
    col[0].write(id)
    # make selected device name bold
    if "selected_device" in state and state.selected_device["id"] == id:
        col[1].write("**"+name+"**")
    else:
        col[1].write(name)
        col[2].write(connection)
        col[3].write(installer)
        col[4].write(compiler)
        col[5].write(model)
        col[6].write(description)
        col[7].button("Delete", key=name, on_click=None, args=(registered_devices, id))
        col[8].button("Modify", key=f'm_{name}', on_click=None, args=(
            registered_devices, id, name, connection, installer, compiler, model, description))
        col[9].button("Select", key=f"s_{name}", on_click=None, args=(
            id, name, connection, installer, compiler, model, description))


