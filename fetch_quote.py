from operator import index
import requests
from bs4 import BeautifulSoup
import random

BASE_LINK = "https://www.greatest-quotations.com/search/quotes-love.html?page="

def random_link():
    rand_num = random.randint(1, 157)
    return f"{BASE_LINK}{rand_num}"
    
def get_quote_text():
    response = requests.get(random_link())
    soup = BeautifulSoup(response.text, 'html.parser')

    quotes = soup.select(".fbquote")
    authors = soup.select(".auteurfbnaam")

    rand = random.randint(0, len(quotes)-1)
    quote = f"{quotes[rand].get_text()} - {authors[rand].get_text()}"
    return quote



