import requests
from image_handling import download_image


def fetch_spacex_launch(images_folder, launch_num=13):
    url = 'https://api.spacexdata.com/v3/launches'

    response = requests.get(url)
    response.raise_for_status()

    links = response.json()[launch_num]['links']['flickr_images']

    for number, link in enumerate(links, start=1):
        path = '{0}/spacex{1}.jpg'.format(images_folder, number)
        download_image(link, path)
