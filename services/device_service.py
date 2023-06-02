import usb.core
import usb.util
import requests
import json
import pandas as pd
import os

from config import BACKEND_URL


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
        except Exception as e:
            print(str(e))
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
    res = requests.post(f"{BACKEND_URL}/add_device/", json=data)
    if res.status_code == 201:
        return None
    return json.loads(res.text)


def get_registered_devices():
    """Return a list of all registered devices on backend"""

    response = requests.get(f"{BACKEND_URL}/registered_devices/")

    if response.text == []:
        raise ValueError()
    else:
        response = json.loads(response.text)

    return response


def remove_device(*args):
    """Removes device from backend based on device_id.

    Args:
        *args: device_id as a tuple
    """

    device_id = ''.join(args)
    response = requests.delete(f"{BACKEND_URL}/remove_device/{device_id}")

    if response.status_code == 400:
        raise ValueError()
