import streamlit as st

from pages.sidebar import sidebar
from services import device_service, bridge_service, installing_service


# Page setup
st.set_page_config(
    page_title="Devices",
    layout="wide"
)

state = st.session_state

def select_device(*args):
    state.device = {
        "id": args[0],
        "name": args[1],
        "connection": args[2],
        "installer": args[3],
        "model": args[4],
        "description": args[5],
        "serial": args[6]
    }
    st.success(
        (f"You have selected **{state.device['name']}"
         f"/ {state.device['connection']}**."
         ))
    # st.success(
    #     f"You have selected **{state.device_name} / {state.installer} / {state.connection}**.")


def remove_device(*args):
    try:
        device_service.remove_device(*args)
        st.success("Device removed successfully.")
    except ValueError:
        st.error("Could not remove device.")


def submit_add():
    device = {
        "name": state.device_name,
        "connection": state.connection,
        "installer_id": state.installer_id,
        "model": state.device_model,
        "description": state.description,
        "serial": state.serial
    }

    for key in device.keys():
        if key in state.keys():
            del state[key]

    added_device = device_service.send_add_request(device)

    if added_device is None:
        st.error("Can not register device. Computer says no.")
        return

    state.device = added_device

    st.success(
        (f"You have added **{state.device['name']}"
         f"/ {state.device['installer']['name']} / {state.device['connection']}**."
         ))


def handle_add(manufacturer="", product="", serialnum=""):
    installers = installing_service.get_installers()
    display = [installer["name"] for installer in installers]
    installer_id = [installer["id"] for installer in installers]
    installer_options = dict(zip(installer_id, display))

    def format_func(option):
        return installer_options[option]

    with st.form("new_device"):
        st.write("Add a new device")
        st.text_input("Device name", key="device_name", value=manufacturer)
        st.text_input("Connection", key="connection")
        state.installer_id = st.selectbox(
            "Installer",
            options=installer_id,
            format_func=format_func
            )
        st.text_input("Model", key="device_model", value=product)
        st.text_input("Description", key="description")
        st.text_input("Serial number", key="serial", value=serialnum)

        add_col, _, _, _, _, cancel_col = st.columns(6)
        add_col.form_submit_button(label="Add", on_click=submit_add)
        cancel_col.form_submit_button(label="Cancel")


def select_bridge(*args):
    print(args)

    if bridge_service.try_conntection(args[2]):
        state.bridge = {
            "id": args[0],
            "name": args[1],
            "address": args[2]
        }
        st.success(f"Successfully selected bridge {state.bridge['name']}")
        return
    st.error(
        "Error while trying to connect to bridge.\n"
        "Please make sure that the bridge is active.")


def remove_bridge(*args):
    try:
        bridge_service.remove_bridge(*args)
        st.success("Bridge removed successfully.")
    except ValueError:
        st.error("Could not remove bridge.")


def register_a_bridge():
    with st.expander("Register a bridging device", expanded=False):
        ip_addr = st.text_input('IP address of the bridging server')
        bridge_name = st.text_input('Name of server (Optional)')
        register = st.button('Add')

        if register:
            added = bridge_service.add_bridge(ip_addr, bridge_name)
            if added is not None:
                error = added["detail"][0]["msg"]
                field = added["detail"][0]["loc"][1]
                st.error((f":red[Error with field] :orange[{field}]: "
                         f":orange[{error}]"))
            else:
                st.success("Bridging device registered successfully! 🔥")


def load_page_info():
    columns = st.columns(4)
    columns[0].title("Device")
    with columns[-1].expander("ℹ️ Help"):
        st.markdown("On this page you can connect to a bridging device.")
        st.markdown(
            "It will eventually also show an overview of connected devices.")


def list_connected_devices():
    st.header("Connected devices")
    st.button("Refresh", key="refresh")

    if "added" in state:
        if state.added is not None:
            error = state.added["detail"][0]["msg"]
            field = state.added["detail"][0]["loc"][1]
            st.write(f":red[Error with field] :orange[{field}]:")
            st.write(f":orange[{error}]")
    devices = device_service.find_usb_devices()
    device_col1, device_col2, device_col3, device_col4 = st.columns(4)

    for i, device in enumerate(devices, start=1):
        device_col1.write(device["manufacturer"])
        device_col2.write(device["product"])
        device_col3.write(device["serial"])
        device_col4.button("Register this device", key=i, on_click=handle_add, args=(
            device["manufacturer"], device["product"], device["serial"]
        ))


def list_registered_bridges():
    st.header("All registered bridges")

    col = st.columns(10, gap="small")

    try:
        registered_bridges = bridge_service.get_registered_bridges()
        col[0].write("Id")
        col[1].write("Address")
        col[2].write("Name")
        for row in registered_bridges.sort_values("id").itertuples():
            _, ip_address, name, id = row
            col = st.columns(10, gap="small")

            col[0].write(id)
            col[1].write(ip_address)
            if "bridge" in state and state.bridge == ip_address:
                col[2].write(f"**:green[{name}]**")
            else:
                col[2].write(name)
            col[3].button("Remove bridge", key=f"r_{ip_address}_{id}",
                          on_click=remove_bridge, args=str(id))
            col[4].button("Select bridge", key=f"s_{ip_address}_{id}",
                          on_click=select_bridge, args=(str(id), name, ip_address))
    except ValueError:
        st.warning("No registered bridges")


def list_registered_devices():
    st.header("All registered devices")

    try:
        registered_devices = device_service.get_registered_devices()

        col = st.columns(11)
        col[0].write("Id")
        col[1].write("Name")
        col[2].write("Connection")
        col[3].write("Installer")
        col[4].write("Model")
        col[5].write("Description")
        col[6].write("Serial number")
        for row in registered_devices.sort_values("id").itertuples():
            col = st.columns(11)
            _, name, connection, installer_id, model, description, serial, id, installer = row
            col[0].write(id)
            # make selected device name bold
            if "device" in state and state.device["id"] == id:
                col[1].write(f"**:green[{name}]**")
            else:
                col[1].write(name)
            col[2].write(connection)
            col[3].write(installer["name"])
            col[4].write(model)
            col[5].write(description)
            col[6].write(serial)
            col[7].button("Remove device", key=f"r_{id}_{name}",
                          on_click=remove_device, args=(
                              str(id)))  # args in st.buttons is always a tuple of strings
            col[8].button("Modify", key=f"m_{id}_{name}", on_click=None,
                          args=(
                              registered_devices, id, name,
                              connection, installer_id, model, description))
            col[9].button("Select device", key=f"s_{id}_{name}",
                           on_click=select_device,
                           args=(
                               id, name, connection,
                               installer_id, model, description, serial))
    except ValueError:
        st.warning("No registered devices.")


def main():
    load_page_info()

    register_a_bridge()

    list_connected_devices()

    list_registered_bridges()

    list_registered_devices()


sidebar.load_side_bar()
main()
