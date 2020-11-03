import requests
from bs4 import BeautifulSoup
import lxml

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
URL = "https://www.walmart.com/ip/Hoover-FH52000-SmartWash-Automatic-Carpet-Cleaner/901855512"

response = requests.get(URL)
soup = BeautifulSoup(response.text, features="lxml")
#format = soup.find_all("meta", text=True)[0].text

description_data = soup.find_all("div", {"class": "about-desc about-product-description xs-margin-top"})
for li in description_data:
    print(li.text)



