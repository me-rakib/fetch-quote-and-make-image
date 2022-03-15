from telethon import TelegramClient
from dotenv import load_dotenv
import os 
import time
from fetch_quote import get_quote_text
from text_to_pic import make_pic_with_text

load_dotenv()  #loding data from .env

api_id = os.getenv("API_ID")
api_hash = os.getenv("API_HASH")
users = os.getenv("MSG_SEND_TO").split(',')

def send_msg():
    # creating picture with quote
    make_pic_with_text(get_quote_text())
    with TelegramClient('anon', api_id, api_hash) as client:
        # sending quote.png to multiple user
        for user in users:
            client.loop.run_until_complete(client.send_file(user, './quote.png'))
            print(f"{time.ctime()}: Message sent to {user}")