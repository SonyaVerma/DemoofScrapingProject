from bs4 import BeautifulSoup, ResultSet
import requests

# retrieve the h1 string
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
URL = "https://www.amazon.com/Fujifilm-Instax-Camera-Sheets-Accessories/dp/B074WH86Y2/ref=sr_1_7?crid=3A7PP9H6854MC&dchild=1&keywords=fujifilm%2Binstax%2Bmini%2Bfilm&qid=1596656102&sprefix=fujifilm%2Caps%2C213&sr=8-7&th=1"
r = requests.get(URL, headers=headers)
soup = BeautifulSoup(r.content, 'lxml')

description_class = soup.select('div[class*="bullet"]')
print(description_class)

# search for ul tags within classes including "bullet"
for i in description_class:
    ul_data = i.find_all("ul")

    # check if li tags nested within ul tags

    for i in ul_data:
        li_data = i.find_all("li")
        if li_data is None:
            print("Fail")

        # print ul data if li tags nested under ul tags

        else:
            print(ul_data)

