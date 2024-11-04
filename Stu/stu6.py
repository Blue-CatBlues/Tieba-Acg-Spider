poem = "众鸟高飞尽，孤云独去闲。相看两不厌，只有敬亭山。"


# 使用集合来检查是否有重复的汉字
words = set()
symbols = {'，', '。'}
 
for char in poem:
    if char in symbols:
        continue  # 跳过符号
    if char in words:
        print("不孤独")
        break
    words.add(char)
else:
    print("孤独")