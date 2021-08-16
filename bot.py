import telegram
import os
import time
from fetch_nasa import fetch_nasa_apod_images, fetch_nasa_epic_images
from fetch_spacex import fetch_spacex_last_launch
from dotenv import load_dotenv


def main():
    load_dotenv()
    fetch_nasa_apod_images()
    fetch_nasa_epic_images()
    fetch_spacex_last_launch()
    bot = telegram.Bot(token=os.environ['BOT_TOKEN'])
    photos = os.listdir('images')
    while True:
        for photo in photos:
            bot.send_photo(
                chat_id=os.environ['CHAT_ID'],
                photo=open('images/{}'.format(photo), 'rb')
            )
            time.sleep(86400)


if __name__ == '__init__':
    main()
