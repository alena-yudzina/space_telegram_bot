from pathlib import Path
from urllib.parse import unquote, urlsplit

import requests


def get_extension(link):
    path = urlsplit(link).path
    return unquote(Path(path).suffix)


def download_image(link, path, params={}):
    print(params)
    response = requests.get(link, params=params)
    response.raise_for_status()
    with open(path, 'wb') as img:
        img.write(response.content)
