import requests
from bs4 import BeautifulSoup
URL = "https://google.com"

r=requests.get(URL).text
soup=BeautifulSoup(r, 'html.parser')

print('\n\033[4mText Content:\033[0m ')
print(soup.get_text())