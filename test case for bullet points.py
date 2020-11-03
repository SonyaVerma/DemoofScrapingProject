from bs4 import BeautifulSoup
import requests

# retrieve the h1 string
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
URL = "https://www.walmart.com/ip/Hoover-FH52000-SmartWash-Automatic-Carpet-Cleaner/901855512"
r = requests.get(URL, headers=headers)
soup = BeautifulSoup(r.content, 'lxml')

formatted_h1 = soup.find_all("h1", text=True)[0].text
print(type(formatted_h1))