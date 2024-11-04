import requests
from bs4 import BeautifulSoup
import jieba


# 读取本地文件并进行文本预处理
with open(r"D:\三国演义\sanguo.txt", 'r', encoding='utf-8') as f1:
    t1 = f1.read()

# 文本预处理（同义词合并）
t1 = t1.replace('孔明曰', '孔明')
t1 = t1.replace('玄德曰', '玄德')
t1 = t1.replace('玄德', '刘备')
t1 = t1.replace('关公', '云长')
t1 = t1.replace('云长', '关羽')

# 结巴分词并过滤单字和虚词
ls = jieba.lcut(t1)
ls = [word for word in ls if len(word) > 1]
excludes = {'不可', '却说', }
ls = [word for word in ls if word not in excludes]

# 统计词频并输出人名出现次数
counts = {}
for word in ls:
    counts[word] = counts.get(word, 0) + 1

items = list(counts.items())
items.sort(key=lambda x: x[1], reverse=True)

for i in range(10):
    word, count = items[i]
    print(f"{word:<10}{count:>5}")
