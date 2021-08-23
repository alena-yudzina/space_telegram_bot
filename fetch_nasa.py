import requests
import os
from datetime import datetime
from image_handling import get_extension, download_image
from dotenv import load_dotenv


def fetch_nasa_apod_images(images_folder, token, count=3):

    url = 'https://api.nasa.gov/planetary/apod'

    payload = {
        'api_key': token,
        'count': count,
    }

    response = requests.get(url, params=payload)
    response.raise_for_status()

    links = [apod['url'] for apod in response.json()]

    for number, link in enumerate(links, start=1):
        path = '{0}/apod{1}{2}'.format(images_folder, number, get_extension(link))
        download_image(link, path)


def fetch_nasa_epic_images(images_folder, token):
    url = 'https://api.nasa.gov/EPIC/api/natural'

    payload = {
        'api_key': token,
    }

    response = requests.get(url, params=payload)
    response.raise_for_status()

    photos = response.json()

    for number, photo in enumerate(photos, start=1):
        photo_datetime = photo['date']
        parsed_datetime = datetime.strptime(photo_datetime, '%Y-%m-%d %H:%M:%S')
        link = 'https://api.nasa.gov/EPIC/archive/natural/{0}/png/{1}.png?api_key={2}'.format(
            parsed_datetime.strftime('%Y/%m/%d'),
            photo['image'],
            payload['api_key']
        )
        path = '{0}/earth{1}.png'.format(images_folder, number)
        download_image(link, path)
