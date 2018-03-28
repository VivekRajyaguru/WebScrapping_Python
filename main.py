from bs4 import BeautifulSoup
import requests
import sys

search = raw_input('Enter Search Term:')
params = {"q": search}
r = requests.get('https://www.google.co.in/search', params=params)

soup = BeautifulSoup(r.text, "html.parser")
#print(soup.prettify()) for Complete HTMl View

divs = soup.findAll("div", {"class":"g"})

for item in divs:
    item_text = item.find("a").text
    item_href = item.find("a").attrs["href"]

    if (item_text and item_href):
        print (item_text)
        print (item_href)
        print (item.find("a").parent)


