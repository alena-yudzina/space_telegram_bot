import requests
from image_handling import download_image


def fetch_spacex_last_launch():
    url = 'https://api.spacexdata.com/v3/launches'

    response = requests.get(url)
    response.raise_for_status()

    links = response.json()[13]['links']['flickr_images']

    for number, link in enumerate(links, start=1):
        path = 'images/spacex{0}.jpg'.format(number)
        download_image(link, path)
