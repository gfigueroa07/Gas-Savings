from bs4 import BeautifulSoup
import requests
import time

url = "https://www.newegg.com/asus-prime-rtx5060ti-o16g-geforce-rtx-5060-ti-16gb-graphics-card-triple-fans/p/N82E16814126795R?Item=N82E16814126795R"

headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0"}

response = requests.get(url, headers=headers, timeout=15)
soup = BeautifulSoup(response.text, 'html.parser')

gpu_price = soup.find_all('span', class_='price-current-label')
price = soup.find_all(string="$")
parent = price[0].parent
strong = parent.find("strong")
final_price = strong.string

print(f"Price for gpu is: {final_price}")

