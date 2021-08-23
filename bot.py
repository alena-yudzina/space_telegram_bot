import os
import time
from pathlib import Path

import telegram
from dotenv import load_dotenv

from fetch_nasa import fetch_nasa_apod_images, fetch_nasa_epic_images
from fetch_spacex import fetch_spacex_launch


def upload_images(images_folder, token, chat_id):
    bot = telegram.Bot(token=token)
    photos = os.listdir(images_folder)
    while True:
        for photo in photos:
            with open('{0}/{1}'.format(images_folder, photo), 'rb') as photo:
                bot.send_photo(
                    chat_id=chat_id,
                    photo=photo
                )
            time.sleep(86400)


def main():
    images_folder = 'images'
    Path(images_folder).mkdir(parents=True, exist_ok=True)
    load_dotenv()
    fetch_nasa_epic_images(images_folder, os.environ['NASA_TOKEN'])
    fetch_nasa_apod_images(images_folder, os.environ['NASA_TOKEN'])
    fetch_spacex_launch(images_folder)
    upload_images(images_folder, os.environ['BOT_TOKEN'], os.environ['CHAT_ID'])
    


if __name__ == '__main__':
    main()
