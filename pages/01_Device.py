import streamlit as st

from services import device_service, bridge_service



# Page setup
st.set_page_config(
    page_title="Devices",
    layout="wide"
)

state = st.session_state

if "bridge" in state:
    st.success(f"Successfully selected bridge {state.bridge}")
elif "bridge_fail" in state:
    st.error("Error while trying to connect to bridge.\n Please make sure that the bridge is active.")

def select_device(*args):
    state.device_id = args[0]
    state.device_name = args[1]
    state.connection = args[2]
    state.installer = args[3]
    state.compiler = args[4]
    state.model = args[5]
    state.description = args[6]
    st.success(f"You have selected **{state.device_id} / {state.device_name} / {state.installer} / {state.connection}**.")

def remove_device(*args):
    try:
        device_service.remove(*args)
        st.success("Device removed successfully.")
    except:
        st.error("Could not remove device.")

        
def submit_add():
    state.added = device_service.send_add_request({
        "name": state.device_name,
        "connection": state.connection,
        "installer": state.installer,
        "compiler": state.compiler,
        "model": state.model,
        "description": state.description
    })


def handle_add(manufacturer="", product="", serial=""):
    with st.form("new_device"):
        st.write("Add a new device")
        st.text_input("Device name", key="device_name", value=manufacturer)
        st.text_input("Connection", key="connection")
        st.text_input("Installer", key="installer")
        st.text_input("Compiler", key="compiler")
        st.text_input("Model", key="model", value=product)
        st.text_input("Description", key="description")

        col1, col2, col3, col4, col5, col6 = st.columns(6)
        col1.form_submit_button(label="Add", on_click=submit_add)
        col6.form_submit_button(label="Cancel")


def select_bridge(*address):
    address = "".join(address)
    if bridge_service.try_conntection(address):
        state.bridge = address
    else:
        state.bridge_fail = "true"


def register_a_bridge():
    with st.expander("Register a bridging device", expanded=False):
        ip_addr = st.text_input('IP address of the bridging server')
        name = st.text_input('Name of server (Optional)')
        register = st.button('Add')

        if register:
            added = bridge_service.add_bridge(ip_addr, name)
            if added is not None:
                error = added["detail"][0]["msg"]
                field = added["detail"][0]["loc"][1]
                st.write(f":red[Error with field] :orange[{field}]:")
                st.write(f":orange[{error}]")
            else:
                st.success("Bridging device registered successfully! 🔥")


def load_page_info():
    col = st.columns(4)
    col[0].title("Device")
    with col[-1].expander("ℹ️ Help"):
        st.markdown("On this page you can connect to a bridging device.")
        st.markdown(
            "It will eventually also show an overview of connected devices.")
        # Documentation has not been brought to this version yet
        # st.markdown("[See the doc page for more info](/Documentation)")


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
    col1, col2, col3, col4 = st.columns(4)

    for i, device in enumerate(devices, start=1):
        col1.write(device["manufacturer"])
        col2.write(device["product"])
        col3.write(device["serial"])
        col4.button("Register this device", key=i, on_click=handle_add, args=(
            device["manufacturer"], device["product"], device["serial"]
        ))


def main():
    load_page_info()

    register_a_bridge()

    list_connected_devices()


main()




st.header("All registered bridges")

registered_bridges = bridge_service.get_registered_bridges()

# col1, col2 = st.columns(2)

col = st.columns(10, gap="small")

if not registered_bridges.empty:
    col[0].write("Address")
    col[1].write("Name")
    for row in registered_bridges.sort_values("address").itertuples():
        _, id, address, name = row
        col = st.columns(10, gap="small")

        col[0].write(id)
        col[1].write(address)
        # if "selected_device" in state and state.selected_device["id"] == id:
        #    col[1].write("**"+name+"**")
        col[2].write(name)
        col[3].button("Select bridge", key=f"s_{address}",
                      on_click=select_bridge, args=(address))

registered_devices = device_service.get_registered_devices()

if registered_devices is None:
    st.warning("No registered devices.")

else:
    st.header("All registered devices")
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
            col[7].button("Remove", key=name, on_click=remove_device, args=(
                str(id)))  # args in st.buttons is always a tuple of strings
            col[8].button("Modify", key=f"m_{name}", on_click=None, args=(
                registered_devices, id, name, connection, installer, compiler, model, description))
            col[9].button("Select", key=f"s_{name}", on_click=select_device, args=(
                id, name, connection, installer, compiler, model, description))

