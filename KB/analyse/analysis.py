import json
import os
import matplotlib.pyplot as plt
from matplotlib import font_manager
with open("D:\\AAAPycharmProjects\\KB\\actors_info.json", 'r',encoding='utf-8') as file:
    data = json.load(file)

# 设置中文字体
    font_path = 'C:\\Windows\\Fonts\\simsun.ttc'
    font_prop = font_manager.FontProperties(fname=font_path)

def constellation(data, font_prop):
    c_num = {}
    for i in data:
        constellation = i.get('constellation')
        if constellation:
            if constellation in c_num:
                c_num[constellation] += 1
            else:
                c_num[constellation] = 1
    print(c_num)

    plt.figure()
    plt.bar(list(c_num.keys()), list(c_num.values()), color='skyblue')
    plt.title("演员们星座分布", fontproperties=font_prop)
    plt.xlabel("星座", fontproperties=font_prop)
    plt.ylabel("个数", fontproperties=font_prop)
    plt.xticks(fontproperties=font_prop, rotation=45)
    plt.show()

def height(data, font_prop):
    h_list = []
    for i in data:
        if i.get('height'):
            h_list.append(i.get('height'))
    print(h_list)

    index = 0
    for i in h_list:
        if i.endswith(" cm"):
            h_list[index] = int(i.replace("cm", ""))
        index += 1
    print(h_list)
    index = 0
    for i in h_list:
        if isinstance(i, str):  # 正确的类型检查
            h_list[index] = int(100 * float(i.replace(" m", "")))
        index += 1
    print(h_list)
    # 初始化身高区间统计
    h_num = {
        "160-165": 0,
        "165-170": 0,
        "170-175": 0,
        "175-180": 0,
        "180-185": 0
    }
    # 统计身高区间
    for height in h_list:
        if 160 < height <= 165:
            h_num["160-165"] += 1
        elif 165 < height <= 170:
            h_num["165-170"] += 1
        elif 170 < height <= 175:
            h_num["170-175"] += 1
        elif 175 < height <= 180:
            h_num["175-180"] += 1
        elif 180 < height <= 185:
            h_num["180-185"] += 1
    print(h_num)

    plt.figure(figsize=(16, 8))

    plt.subplot(1, 2, 1)
    plt.bar(list(h_num.keys()), list(h_num.values()), color='pink')
    plt.title("演员们身高分布", fontproperties=font_prop)
    plt.xlabel("身高", fontproperties=font_prop)
    plt.ylabel("个数", fontproperties=font_prop)
    plt.xticks(fontproperties=font_prop, rotation=45)

    plt.subplot(1, 2, 2)
    plt.pie(list(h_num.values()), labels=list(h_num.keys()), autopct='%1.1f%%')
    plt.title("演员们身高分布", fontproperties=font_prop)
    plt.axis('equal')  # 确保饼图为圆形
    plt.show()


def weight(data, font_prop):
    w_list = []

    # 提取体重数据
    for i in data:
        if i.get('weight'):
            w_list.append(i.get('weight'))

            # 转换体重单位
    for i in range(len(w_list)):
        if w_list[i].endswith(" kg"):
            w_list[i] = int(float(w_list[i].replace(" kg", "")))
        elif w_list[i].endswith(" 公斤"):
            w_list[i] = int(float(w_list[i].replace(" 公斤", "")))

            # 初始化体重区间统计
    w_num = {
        "40-50": 0,
        "50-60": 0,
        "60-70": 0,
        "70-80": 0,
        "80-90": 0,
        "90-100": 0,
        "100-110": 0
    }

    # 统计体重区间
    for weight in w_list:
        if 40 < weight <= 50:
            w_num["40-50"] += 1
        elif 50 < weight <= 60:
            w_num["50-60"] += 1
        elif 60 < weight <= 70:
            w_num["60-70"] += 1
        elif 70 < weight <= 80:
            w_num["70-80"] += 1
        elif 80 < weight <= 90:
            w_num["80-90"] += 1
        elif 90 < weight <= 100:
            w_num["90-100"] += 1
        elif 100 < weight <= 110:
            w_num["100-110"] += 1

    print(w_num)

    # 可视化体重分布
    plt.figure(figsize=(16, 8))

    plt.subplot(1, 2, 1)
    plt.bar(list(w_num.keys()), list(w_num.values()), color='lightblue')
    plt.title("体重分布", fontproperties=font_prop)
    plt.xlabel("体重区间 (kg)", fontproperties=font_prop)
    plt.ylabel("个数", fontproperties=font_prop)
    plt.xticks(fontproperties=font_prop, rotation=45)

    plt.subplot(1, 2, 2)
    plt.pie(list(w_num.values()), labels=list(w_num.keys()), autopct='%1.1f%%')
    plt.title("体重分布比例", fontproperties=font_prop)
    plt.axis('equal')  # 确保饼图为圆形
    plt.show()

def main():
    while True:
        os.system('cls')
        print("\n请选择操作:")
        print("1. 显示演员星座分布")
        print("2. 显示演员身高分布")
        print("3. 显示演员体重分布")
        print("0. 退出程序")
        print("#"
              "————温馨提示：若是没有json文件请先运行相应的爬虫————")
        choice = input("请输入选项 (1-3 或 0 退出): ")
        if choice == '1':
            constellation(data, font_prop)
        elif choice == '2':
            height(data, font_prop)
        elif choice == '3':
            weight(data, font_prop)
        elif choice == '0':
            print("谢谢使用！退出程序。")
            break
        else:
            print("无效选项，请重新输入。")

# 运行主程序
if __name__ == "__main__":
    main()