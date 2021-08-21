import requests
from pathlib import Path
from urllib.parse import urlsplit, unquote


def get_extension(link):
    path = urlsplit(link).path
    return unquote(Path(path).suffix)


def download_image(link, path):
    response = requests.get(link)
    with open(path, 'wb') as img:
        img.write(response.content)
