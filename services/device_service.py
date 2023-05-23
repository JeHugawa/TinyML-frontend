import usb.core
import usb.util
import requests
import os
import json
from dotenv import load_dotenv

load_dotenv()

BACKEND_URL = os.getenv("BACKEND_URL")  # "http://backend:8000/"

ACCEPTED_VENDORS = ["Raspberry Pi", "Arduino"]


def find_usb_devices():
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
    data = {key: val if len(val) > 0 else None for key, val in data.items()}
    res = requests.post(f"{BACKEND_URL}/add_device/", json=data)
    if res.status_code == 200:
        return None
    return json.loads(res.text)
