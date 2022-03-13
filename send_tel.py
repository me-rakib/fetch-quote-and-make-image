from telethon import TelegramClient
from dotenv import load_dotenv
import os 
from get_quote_text import get_quote
from text_to_pic import get_quote_pic

load_dotenv() 



api_id = os.getenv("API_ID")
api_hash = os.getenv("API_HASH")
send_to_u_1 = os.getenv("SEND_MSG_U_1")
send_to_u_2 = os.getenv("SEND_MSG_U_2")

def send_msg():
    get_quote_pic(get_quote())
    with TelegramClient('anon', api_id, api_hash) as client:
        client.loop.run_until_complete(client.send_file(send_to_u_2, './quote.png'))
        # client.loop.run_until_complete(client.send_file(send_to_u_1, './quote.png'))