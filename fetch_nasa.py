import requests
from datetime import datetime
from fetch_spacex import get_extension, download_image


def fetch_nasa_apod_images():
    url = 'https://api.nasa.gov/planetary/apod'

    payload = {
        'api_key': 'gbkaDY0eUaTXykPqC8gaKsBxruzU65uHgd29g0DG',
        'count': 3,
    }

    response = requests.get(url, params=payload)
    response.raise_for_status()

    links = [dct['url'] for dct in response.json()]

    for number, link in enumerate(links):
        path = 'images/apod{0}{1}'.format(number + 1, get_extension(link))
        download_image(link, path)


def fetch_nasa_epic_images():
    url = 'https://api.nasa.gov/EPIC/api/natural'

    payload = {
        'api_key': 'gbkaDY0eUaTXykPqC8gaKsBxruzU65uHgd29g0DG',
    }

    response = requests.get(url, params=payload)
    response.raise_for_status()

    photos_info = response.json()

    for number, photo_info in enumerate(photos_info):
        datetime_str = photo_info['date']
        datetime_obj = datetime.strptime(datetime_str, '%Y-%m-%d %H:%M:%S')
        link = 'https://api.nasa.gov/EPIC/archive/natural/{0}/{1}/{2}/png/{3}.png?api_key={4}'.format(
            datetime_obj.year,
            str(datetime_obj.month).zfill(2),
            str(datetime_obj.day).zfill(2),
            photo_info['image'],
            payload['api_key']
        )
        path = 'images/earth{0}.png'.format(number + 1)
        download_image(link, path)
