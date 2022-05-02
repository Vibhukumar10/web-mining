import requests
from bs4 import BeautifulSoup
URL = "https://google.com"

r=requests.get(URL).text
soup=BeautifulSoup(r, 'html.parser')

print('\n\033[4mTitle Tag:\033[0m ')
print(soup.head.title)

print('\n\033[4mp Tags:\033[0m ')
p_tags=soup.find_all('p')
for text in p_tags:
    print(text,end="")
    print('\n')


print('\n\033[4ma Tags:\033[0m ')
a_tags=soup.find_all('a')
for text in a_tags:
    print(text,end="")
    print('\n')

print('\n\033[4mdiv Tags:\033[0m ')
div_tags=soup.find_all('div')
for text in div_tags:
    print(text,end="")
    print('\n')

