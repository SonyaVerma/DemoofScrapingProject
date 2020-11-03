from bs4 import BeautifulSoup
import requests

# retrieve the h1 string
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
URL = "https://www.walmart.com/ip/BISSELL-Proheat-2X-Revolution-Carpet-Cleaner-with-Antibacterial-Formula-1551/46597972?athcpid=46597972&athpgid=athenaItemPage&athcgid=null&athznid=PWVAV&athieid=v0&athstid=CS020&athguid=c2dc714b-007-173c1fb7cdf230&athancid=null&athena=true"
r = requests.get(URL, headers=headers)
soup = BeautifulSoup(r.content, 'lxml')

# search for all classes which contain the string "description"
description_class = soup.select('div[class*="description"]')

# search for ul tags within classes including "description"
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




