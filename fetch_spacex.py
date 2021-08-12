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


def fetch_spacex_last_launch():
    url = 'https://api.spacexdata.com/v3/launches'

    response = requests.get(url)
    response.raise_for_status()

    links = response.json()[13]['links']['flickr_images']

    for number, link in enumerate(links):
        path = 'images/spacex{0}.jpg'.format(number + 1)
        download_image(link, path)
