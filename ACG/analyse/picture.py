import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.font_manager import FontProperties

# 设置中文字体
font = FontProperties(fname='C:\\Windows\\Fonts\\simhei.ttf')  # 你可以根据实际情况调整字体路径

# 读取 Excel 文件
df = pd.read_excel('D:\\AAAPycharmProjects\\ACG\\acg_output.xlsx')

# 提取关注人数并转换为数组
members = df['关注人数'].to_numpy()

# 按照关注人数降序排序
members_sorted = np.sort(members)[::-1]

# 绘制折线图
plt.figure(figsize=(10, 6))
plt.plot(members_sorted, marker='o')

# 设置 y 轴范围
plt.yscale('log')
plt.ylim(10**3, 10**7)

# 添加标题和标签
plt.title('关注人数折线图', fontproperties=font)
plt.xlabel('排名', fontproperties=font)
plt.ylabel('关注人数', fontproperties=font)

# 显示图表
plt.show()
