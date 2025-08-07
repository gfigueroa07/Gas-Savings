from bs4 import BeautifulSoup
import requests

url = "https://www.gasbuddy.com/gasprices/pennsylvania/scranton"
# url = "https://gasprices.aaa.com/?state=PA"
headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0"}
response = requests.get(url, headers=headers) 
soup = BeautifulSoup(response.text, 'html.parser')
# print(soup.prettify())
gas_price = soup.find_all('div', class_="StationDisplayPrice-module__price___3rARL")
# gas_price = soup.find_all('div', class_="main-content")
print(response)
print(gas_price)

# for price in gas_price:
#     print(price)