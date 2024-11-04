import jieba
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# 三国演义文档路径
content_path = r"D:\三国演义\sanguo.txt"

# 人物列表
characters = [
    '曹操', '刘备', '孙权', '孔明', '关羽', '张飞', '赵云', '马超', '黄忠', '周瑜',
    '吕布', '貂蝉', '袁绍', '袁术', '董卓', '孙策', '孙坚', '曹丕', '曹植', '曹仁',
    '曹洪', '夏侯惇', '夏侯渊', '司马懿', '司马昭', '司马师', '郭嘉', '荀彧', '荀攸', '贾诩',
    '张辽', '徐晃', '张郃', '文丑', '颜良', '华雄', '吕蒙', '陆逊', '甘宁', '黄盖',
    '程普', '太史慈', '鲁肃', '庞统', '法正', '蒋琬', '费祎', '魏延', '黄月英', '孟获',
    '祝融夫人'
]

# 将人物列表添加到jieba词典中
for character in characters:
    jieba.add_word(character)

# 读取文章
with open(content_path, "r", encoding='utf-8') as f_content:
    content = f_content.read()

# 文本预处理（同义词合并）
content = content.replace('孔明曰', '孔明')
content = content.replace('玄德曰', '玄德')
content = content.replace('玄德', '刘备')
content = content.replace('诸葛亮', '孔明')
content = content.replace('亮曰', '孔明')
content = content.replace('关公', '云长')
content = content.replace('云长', '关羽')
content = content.replace('孟德', '曹操')
content = content.replace('曹孟德', '曹操')
content = content.replace('曹丕曰', '曹丕')
content = content.replace('仲达', '司马懿')

# 分词
words = jieba.lcut(content)

# 统计词频
counts = {}
for word in words:
    if len(word) == 1:
        continue
    if word in characters:
        counts[word] = counts.get(word, 0) + 1

# 输出词频最高的前10个人物
items = list(counts.items())
items.sort(key=lambda x: x[1], reverse=True)
for i in range(10):
    word, count = items[i]
    print(f"{word:<10}{count:>5}")

# 生成词云
wordcloud = WordCloud(font_path='simhei.ttf', width=800, height=400, background_color='white').generate_from_frequencies(counts)

# 显示词云
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()
