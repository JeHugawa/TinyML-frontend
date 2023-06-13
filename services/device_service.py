import os
from subprocess import Popen, PIPE, STDOUT
import requests
import pandas as pd

from config import BACKEND_URL, ACCEPTED_VENDORS


def find_usb_devices():
    """Find connected usb devices, that are either Arduinos or Raspberry Pis.

    Uses external command 'lsusb' to find USB devices. This is in order to
    find usb devices dynamically in a docker container.

    Script, which finds wanted devices, is based on the output of lsusb. Using
    the amount of whitespace in front of each line we can determine
    what device that row belongs to. A new device always has 0 whitespace
    in front of it, while device information has at least 1 whitespace.

    More elegant solution would be to create a dictionary from the output,
    however, this solution works perfectly fine.

    TODO:
        Windows support

    Returns:
        Function returns the found connected usb devices
    """

    # A predetermined output for robot framework tests
    if os.environ.get("ROBOT_TESTS") == "true":
        return [{'manufacturer': 'Arduino',
                 'product': 'Nano 33 BLE',
                 'serial': '707B266C064B14F6'}]

    p = Popen("lsusb -v", shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT)
    output = p.stdout.read()

    out = output.decode('utf-8').split('\n')
    find_variables = False

    return_devices = []

    for row in out:
        if len(row) == 0:
            continue
        if (row[0] != " " and
                len([row for vendor in ACCEPTED_VENDORS if vendor.lower() in row.lower()]) > 0):
            find_variables = True
            return_devices.append({})
        elif row[0] != " " and "arduino" not in row.lower() and "Device Descriptor" not in row:
            find_variables = False
        elif find_variables:
            row = row.split()
            if row[0] == "iManufacturer" or row[0] == "iSerial" or row[0] == "iProduct":
                return_devices[-1][row[0][1:].lower()] = " ".join(row[2:])

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

    if response.text == '[]':
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
