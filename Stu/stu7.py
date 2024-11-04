import re
from collections import Counter
from jiayan import load_lm, CharHMMTokenizer

# 读取文件内容
with open('D:\\ThreeKingdomsHumans.txt', 'r', encoding='ANSI') as file:
    text = file.read()

# 去除符号和标点
text = re.sub(r'[^\w\s]', '', text)

# 加载甲言的语言模型
lm = load_lm('path_to_your_jiayan_model/jiayan.klm')
tokenizer = CharHMMTokenizer(lm)

# 使用甲言分词
words = list(tokenizer.tokenize(text))

# 定义要跳过的词语列表
skip_words = ['曰', '之', '也', '吾', '与', '将', '而', '了', '有']

# 过滤掉要跳过的词语
filtered_words = [word for word in words if word not in skip_words]

# 统计每个词语出现的次数
word_counts = Counter(filtered_words)

# 找出最常见的10个词语及其次数
most_common_words = word_counts.most_common(10)

# 输出结果
for word, count in most_common_words:
    print(f'{word}: {count}')
