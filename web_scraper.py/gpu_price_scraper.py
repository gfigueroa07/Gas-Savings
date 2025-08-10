from bs4 import BeautifulSoup
import requests
import time
from selenium import webdriver



web_scraper = webdriver.Chrome()
web_scraper.get("https://www.newegg.com/pny-technologies-inc-verto-vcg4070ts16tfxxpb1-o-geforce-rtx-4070-ti-super-16gb-graphics-card-triple-fans/p/N82E16814133866")

time.sleep(5)

html = web_scraper.page_source
soup = BeautifulSoup(html, 'html.parser')


gpu_price = soup.find_all('span', class_='price-current-label')
price = soup.find_all(string='$')
parent = price[0].parent
strong = parent.find("strong")
final_price = strong.string
print(f"Price for gpu is: {final_price}")


# url = "https://www.newegg.com/pny-technologies-inc-verto-vcg4070ts16tfxxpb1-o-geforce-rtx-4070-ti-super-16gb-graphics-card-triple-fans/p/N82E16814133866"

# user_agents = [
#     "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
#     "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
#     "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
#     "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Firefox/108.0",
#     "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15"
# ]

# headers = {
#     'User-Agent': random.choice(user_agents),
#     # "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
#     "Accept": "application/json, text/plain, */*",
#     "Accept-Language": "en-US,en;q=0.9",
#     "Cache-Control": "no-cache",
#     "Pragma": "no-cache",
#     }

# response = requests.get(url, headers=headers, timeout=15)
# soup = BeautifulSoup(response.text, 'html.parser')

# gpu_price = soup.find_all('ul', class_='price')
# price = soup.find_all(string='$')

# parent = price[0].parent
# strong = parent.find("strong")
# final_price = strong.string
# print(f"Price for gpu is: {final_price}")

# # print(soup.prettify())
# # print(response.text)  # Uncomment for debugging full HTML


