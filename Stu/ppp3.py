
import requests
from bs4 import BeautifulSoup
url = 'https://hongloumeng.5000yan.com/hlm1127.html'
req=requests.get(url)
soup=BeautifulSoup(req.content, 'html.parser')
soup_texts=soup.find('div',class_='grap')
for link in soup_texts:
    if link!='\n':

        print(link.text,end="")


