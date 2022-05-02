import requests
from bs4 import BeautifulSoup
URL = "https://google.com"

r=requests.get(URL)
soup=BeautifulSoup(r.content, 'html5lib')

print('\n\033[4mRaw HTML Content:\033[0m ')
print(soup.prettify())