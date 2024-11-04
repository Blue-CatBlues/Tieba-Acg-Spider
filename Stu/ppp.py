
import requests
from bs4 import BeautifulSoup
url = 'https://hongloumeng.5000yan.com'
req=requests.get(url)
soup=BeautifulSoup(req.content)
soup_texts=soup.find('div',class_='p-2 my-2 bg-white rounded')
for link in soup_texts.ul.children:
    if link!='\n':

        print(link.text+":",link.a.get('href'))