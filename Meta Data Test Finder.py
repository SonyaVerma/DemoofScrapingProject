from bs4 import BeautifulSoup
import requests

# retrieve the h1 string
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
URL = "https://www.walmart.com/ip/Hoover-FH52000-SmartWash-Automatic-Carpet-Cleaner/901855512"
r = requests.get(URL, headers=headers)
soup = BeautifulSoup(r.content, 'lxml')

formatted_h1 = soup.find_all("h1", text=True)[0].text
#print(format)

for i in formatted_h1:

    # retrieve the meta data

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    URL = "https://www.walmart.com/ip/Hoover-FH52000-SmartWash-Automatic-Carpet-Cleaner/901855512"

    response = requests.get(URL)
    soup = BeautifulSoup(response.text, features="lxml")
    description_data = soup.find_all("div", {"class": "about-desc about-product-description xs-margin-top"})
    for li in description_data:
        meta_data = li.text
        #print(meta_data)

    # see if meta data perfectly matches h1

    for i in meta_data:
        if meta_data == formatted_h1:
            print(format.append("Priority 1"))

        # see if anything in meta data matches h1

        elif meta_data != formatted_h1:
            smallstring = str(formatted_h1)
            bigstring = str(meta_data)

            # convert the h1 string into a list
            def convert(string):
                li = list(string.split(" "))
                return li
            str1 = smallstring

            # see if any h1 list elements found in meta data

            res = [ele for ele in str1 if(ele in meta_data)]
            print(formatted_h1 + " Priority 2 ")

        else:
            print("No title match!")
