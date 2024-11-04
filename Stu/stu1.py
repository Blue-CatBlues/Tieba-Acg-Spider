import random

bool_1 = True
bool_2 = False
print(f"bool_1的变量类型为{type(bool_1)}", end="")
print(f"bool_1的变量类型为{type(bool_1)}", end="\n")
print(f"bool_1的变量类型为{type(bool_1)}", end="")
print(f"bool_1的变量类型为{type(bool_1)}", end="\t")
print(f"bool_1的变量类型为{type(bool_1)}")

# random
a = random.randint(1, 100)
# 小数
b = random.uniform(1, 100)
# 从0到1的一个小数
c = random.random()
print(f"{a}\t{b}\t{c}")

# 除法后为小数会自动转换类型 整型——浮点型
a_1 = 1
a_1 /= 2
print(f"{a_1}")

# 与或非
a__1 = True
a__2 = not a__1
print(f"{a__1}\t{a__2}")

# for循环
for i in range(10):
    print(f"{i}\t", end="")

arr = [1, 2, 3]
for i in arr:
    print(f"{i}\t", end="")

str = "asdfg"
for i in str:
    print(f"{i}\t", end="")

# 截取
str = "hello word where are you"
a = str[1:20:3]  # 下标1到19，隔2位截取
print(a)

a = str[::-1]  # 翻转
print(a)

a = str[-1:-10:-1]   # 从倒数下标第1个截取到倒数下标第9个
print(a)


# 替换
str_1 = str.replace("hello","hi")
print(str_1)


# 分割字符串
arr = str.split("  ")
print(arr)

str__3 = " _".join(arr)
print(str__3)

a = "hello".capitalize()  # 将字符串第一个字母转换成大写
a = "hello".title()       # 将字符串每个单词首字母转换成大写
a = "hello".lower()       # 将字符串中大写转小写
a = "hello".upper()       # 将字符串中小写转大写

# 删除空白字符:
b = " hello".lstrip()     # 删除字符串左侧空白字符
b = "hello ".rstrip()     # 删除字符串右侧空白字符
b = " hello ".strip()     # 删除字符串两侧空白字符

array = [
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
    [[3, 2, 5], [4, 5, 8], [7, 8, 9]],
    [[1, 2, 3], [4, 5, 8], [7, 0, 9]]
]

for a in array:
    for b in a:
        for c in b:
            print(f"{c}\t", end="")

# 元组
a = (1, 2, 3)
# 只读列表，不可被修改

# 集合 重复的元素会被自动删除
a = {1, 2, 3}
a.add(6)
# 字典
d = {"name": "Pig", "age": 20}

d.keys()    # ['name', 'age']
d.values()  # ['Pig', 20]
d.items()   # [('name', 'Pig'), ('age', 20)]

#函数
def day():
    print("起床了")
    print("吃早餐")
    print("上班去")
    print("睡觉")

a = True


for i in range(4):
    day()

if a:
    day()

 