from bs4 import BeautifulSoup
import requests

# retrieve the h1 string
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
URL = "https://www.walmart.com/ip/Hoover-FH52000-SmartWash-Automatic-Carpet-Cleaner/901855512"
r = requests.get(URL, headers=headers)
soup = BeautifulSoup(r.content, 'lxml')

# search = [li for li in (ul.find('li') for ul in soup.findAll('ul')) if li]
# print(search)

# find ul data
ul_data = soup.findAll("ul")
updated_ul = str(ul_data)
# print(ul_data)

# search for li tags within ul
search = [li for li in (ul.find('li') for ul in soup.findAll('ul')) if li]
print(search)

# if search returns, find if parent class has "description" in it
if search == search:
    for li in search:
        li_data = str(li.text)
        print(li_data)
    for search in soup.select('div[class*="description"]'):
        print(search.get_text())
            #li in ul_data:
       # if "description" in li.parent.name:
         #   print(li.parent.name)
    #for li in ul_data:
        #return li.parent.name


        #search = [li for li in (ul.find('li') for ul in soup.findAll('ul')) if li]

        #print(parent)

# if tag == tag:

# for li in ul_data:
# li_data = str(li.text)
# print(li_data)


# all_children = first_child.findChildren()
# print(all_children)
