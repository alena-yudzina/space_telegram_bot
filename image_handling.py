import requests
from pathlib import Path
from urllib.parse import urlsplit


def get_extension(link):
    path = urlsplit(link).path
    return Path(path).suffix


def download_image(link, path):
    response = requests.get(link)
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    with open(path, 'wb') as img:
        img.write(response.content)
