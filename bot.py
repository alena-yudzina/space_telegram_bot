import telegram
import os
from pathlib import Path
import time
from fetch_nasa import fetch_nasa_apod_images, fetch_nasa_epic_images
from fetch_spacex import fetch_spacex_last_launch
from dotenv import load_dotenv


def upload_images(images_folder):
    bot = telegram.Bot(token=os.environ['BOT_TOKEN'])
    photos = os.listdir(images_folder)
    while True:
        for photo in photos:
            with open('{0}/{1}'.format(images_folder, photo), 'rb') as photo:
                bot.send_photo(
                    chat_id=os.environ['CHAT_ID'],
                    photo=photo
                )
            time.sleep(86400)


def main():
    images_folder = 'images'
    Path(images_folder).mkdir(parents=True, exist_ok=True)
    load_dotenv()
    fetch_nasa_apod_images(images_folder)
    fetch_nasa_epic_images(images_folder)
    fetch_spacex_last_launch(images_folder)
    upload_images(images_folder)
    


if __name__ == '__main__':
    main()
