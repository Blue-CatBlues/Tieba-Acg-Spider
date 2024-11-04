# 632307110105 刘烨
import jieba
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import requests
from bs4 import BeautifulSoup

url = 'https://sanguo.5000yan.com/'

req = requests.get(url)
soup = BeautifulSoup(req.content, 'html.parser')
soup_texts = soup.find('div',class_='p-3 my-2 bg-white rounded')
# 保存章节内容
with open(r'D:\三国演义\sanguo.txt', "w", encoding='utf-8') as f:
    for link in soup_texts.ul.children:
        if link != '\n':
            # 在html里获取对应章节的url
            content_url = link.a.get('href')
            try:
                # 重复上述步骤 保存目录内的url 接着爬取每一章的具体内容
                con_d_req = requests.get(content_url)
                con_d_soup = BeautifulSoup(con_d_req.content, 'html.parser')
                con_d_soup_texts = con_d_soup.find('div', class_='grap')
                # 先写入章节标题，再写入内容
                f.write('\n\n' + link.text + ': ' + '\n\n')
                f.write(con_d_soup_texts.text)
            except Exception as e:
                print(f"无法下载 {link.text}: {e}")
f.close()

content_path = r"D:\三国演义\sanguo.txt"

# 列出热门人物列表
character_list = [
    '曹操', '刘备', '孙权', '孔明', '关羽', '张飞', '赵云', '马超', '黄忠', '周瑜',
    '吕布', '貂蝉', '袁绍', '袁术', '董卓', '孙策', '孙坚', '曹丕', '曹植', '曹仁',
    '曹洪', '夏侯惇', '夏侯渊', '司马懿', '司马昭', '司马师', '郭嘉', '荀彧', '荀攸', '贾诩',
    '张辽', '徐晃', '张郃', '文丑', '颜良', '华雄', '吕蒙', '陆逊', '甘宁', '黄盖',
    '程普', '太史慈', '鲁肃', '庞统', '法正', '蒋琬', '费祎', '魏延', '黄月英', '孟获',
    '祝融夫人'
]

for character in character_list:
    jieba.add_word(character)

with open(content_path, "r", encoding='utf-8') as f:
    content = f.read()
    # 把重复的人名先修改
    content = content.replace('孔明曰', '孔明')
    content = content.replace('玄德曰', '玄德')
    content = content.replace('玄德', '刘备')
    content = content.replace('备曰', '刘备')
    content = content.replace('刘备曰', '刘备')
    content = content.replace('诸葛亮', '孔明')
    content = content.replace('亮曰', '孔明')
    content = content.replace('关公', '云长')
    content = content.replace('云长', '关羽')
    content = content.replace('孟德', '曹操')
    content = content.replace('孟德曰', '曹操')
    content = content.replace('曹孟德', '曹操')
    content = content.replace('曹丕曰', '曹丕')
    content = content.replace('仲达', '司马懿')

# 分词
words = jieba.lcut(content)

# 统计词频
num = {}
for word in words:
    # 如果是单字词直接跳过，不可能是人名
    if len(word) == 1:
        continue
    # 对照人名列表添加词频
    if word in character_list:
        num[word] = num.get(word, 0) + 1

# 输出词频最高的前10个人物
items = list(num.items())
items.sort(key=lambda x: x[1], reverse=True)
for i in range(10):
    word, count = items[i]
    # 格式对齐输出
    print(f"{word:<10}{count:>5}")

# 生成词云
wordcloud = WordCloud(font_path='simhei.ttf', width=1200, height=600, background_color='white').generate_from_frequencies(num)
plt.figure(figsize=(16, 9))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()
