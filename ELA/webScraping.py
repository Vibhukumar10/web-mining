import requests
from bs4 import BeautifulSoup
URL = "https://en.wikipedia.org/wiki/Apple_Inc."

r=requests.get(URL)
soup=BeautifulSoup(r.content,'html5lib')

print(soup.prettify())