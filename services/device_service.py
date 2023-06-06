import os
import usb.core
import usb.util
import requests
import pandas as pd

from config import BACKEND_URL, ACCEPTED_VENDORS


def find_usb_devices():
    """Find connected usb devices, that are either Arduinos or Raspberry Pis.

    This requires root privileges, and when running in a docker container,
    only devices that are connected when container is started can be found.

    Returns:
        Function returns the found connected usb devices
    """

    if os.environ.get("ROBOT_TESTS") == "true":
        return [{'manufacturer': 'Arduino',
                 'product': 'Nano 33 BLE',
                 'serial': '707B266C064B14F6'}]

    all_devices = list(usb.core.find(find_all=True))

    devices = []

    for device in all_devices:
        try:
            if (usb.util.get_string(device, device.iManufacturer)
                    in ACCEPTED_VENDORS):
                devices.append(device)
        except Exception as error:  # pylint: disable=broad-exception-caught
            print(str(error))
            continue

    return_devices = []
    for device in devices:
        manufacturer = usb.util.get_string(
            device, device.iManufacturer)
        product = usb.util.get_string(device, device.iProduct)
        serial = usb.util.get_string(device, device.iSerialNumber)

        return_devices.append({"manufacturer": manufacturer,
                               "product": product,
                               "serial": serial})

    return return_devices


def send_add_request(data: dict):
    """Send the request to add the device to the backend

    Args:
        data: The data of the device
    """

    data = {key: val if len(val) > 0 else None for key, val in data.items()}
    res = requests.post(f"{BACKEND_URL}/devices/", json=data, timeout=5)
    if res.status_code == 201:
        return res.json()
    return None


def get_registered_devices():
    """Return a list of all registered devices on backend"""

    response = requests.get(f"{BACKEND_URL}/devices/", timeout=5)

    if response.text == []:
        raise ValueError()
    devices = pd.read_json(response.text)

    return devices


def get_no_of_devices():
    """Calculates number of devices in device list.
    """
    
    devices = pd.DataFrame(get_registered_devices())

    return devices.shape[0]


def remove_device(*args):
    """Removes device from backend based on device_id.

    Args:
        *args: device_id as a tuple
    """

    device_id = "".join(args)
    response = requests.delete(f"{BACKEND_URL}/devices/{device_id}", timeout=5)

    if response.status_code == 400:
        raise ValueError()
