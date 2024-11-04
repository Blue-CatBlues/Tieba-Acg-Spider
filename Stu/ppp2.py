# 刘烨 63230711015
import requests
from bs4 import BeautifulSoup

url = 'http://hongloumeng.5000yan.com/'

# 目录页请求
req = requests.get(url)
soup = BeautifulSoup(req.content, 'html.parser')
soup_texts=soup.find('div',class_='p-2 my-2 bg-white rounded')
# 保存章节内容
with open(r'D:\红楼梦\hongloumeng.txt', "w", encoding='utf-8') as f:
    for link in soup_texts.ul.children:
        if link != '\n':
            download_url = link.a.get('href')
            try:
                download_req = requests.get(download_url)
                download_soup = BeautifulSoup(download_req.content, 'html.parser')
                download_soup_texts = download_soup.find('div', class_='grap')
                f.write('\n\n' + link.text + ': ' + '\n\n')
                f.write(download_soup_texts.text)
            except Exception as e:
                print(f"无法下载 {link.text}: {e}")
f.close()