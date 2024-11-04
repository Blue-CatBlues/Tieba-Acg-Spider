import jieba

# 红楼梦文档路径
content_path = r'D:\红楼梦\hongloumeng.txt'

# 人物列表
characters = [
    '贾宝玉', '林黛玉', '薛宝钗', '贾母', '王夫人', '王熙凤', '贾政', '贾赦', '贾琏', '贾探春',
    '贾迎春', '贾惜春', '李纨', '妙玉', '史湘云', '秦可卿', '晴雯', '袭人', '鸳鸯', '紫鹃',
    '平儿', '香菱', '金钏', '司棋', '抱琴', '赖大', '焦大', '王善保', '周瑞', '林之孝', '乌进孝',
    '包勇', '吴贵', '吴新登', '邓好时', '王柱儿', '余信'
]

# 将人物列表添加到jieba词典中
for character in characters:
    jieba.add_word(character)

# 读取文章
with open(content_path, "r", encoding='utf-8') as f_content:
    content = f_content.read()

# 分词
words = jieba.lcut(content)

# 统计词频
counts = {}
for word in words:
    if len(word) == 1:
        continue
    counts[word] = counts.get(word, 0) + 1

# 输出词频最高的前10个词
items = list(counts.items())
items.sort(key=lambda x: x[1], reverse=True)
for i in range(10):
    word, count = items[i]
    print(f"{word:<10}{count:>5}")
