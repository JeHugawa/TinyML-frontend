import json
import requests

from config import BACKEND_URL


def get_installers():
    """Return a list of all registered / allowed installers"""

    response = requests.get(f"{BACKEND_URL}/installers/", timeout=5)

    if response.text == '[]':
        raise ValueError()
    devices = json.loads(response.text)

    return devices
