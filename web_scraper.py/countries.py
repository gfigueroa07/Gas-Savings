# Scraping countrie's population cuz why not... let a mf be happy i know its faster to search on google...

import requests, random
from bs4 import BeautifulSoup


user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Firefox/108.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15"
]

headers = {
    'User-Agent': random.choice(user_agents),
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "en-US,en;q=0.9",
    "Cache-Control": "no-cache",
    "Pragma": "no-cache",
    }

url = "https://www.scrapethissite.com/pages/simple/"

requests = requests.get(url, headers=headers, timeout=15)
soup = BeautifulSoup(requests.text, 'html.parser')

countries = soup.find_all('div', class_='col-md-4 country')
def country_output():
    opt = input(f"What country you want to get population from?\n")
    while True:
        try:
            for country in countries:
                if opt in country.text:
                    print(country.text)
                    return True
            print("Country not found. Please check spelling.\nExample:\nIf looking for 'united states', Make sure to type 'United States'.")
            return False
        except Exception as e:
            print("Error: ", e)
country_output()