import matplotlib.pyplot as plt

# 创建画布
Fig1 = plt.figure()
x = [1, 2, 3, 4, 5] # 定义x轴的数据
y = [1, 8, 27, 64, 125] # 定义y轴的数据

plt.plot(x, y) # plot函数：画图，可定制化
plt.show()

# 定义数据
x = [1, 2, 3, 4, 5]  # 定义x轴的数据
y1 = [1, 4, 9, 16, 25]  # 定义y1的数据
y2 = [1, 8, 27, 64, 125]  # 定义y2的数据
y3 = [1, 2, 3, 4, 5]  # 定义y3的数据

# Matlab 画图
fig1 = plt.figure()
plt.plot(x, y1, label='y1')  # 添加标签
plt.plot(x, y2, label='y2')  # 添加标签
plt.plot(x, y3, label='y3')  # 添加标签
plt.legend()  # 显示图例
plt.show()  # 显示图像

# 面向对象方式
fig2 = plt.figure()
ax2 = plt.axes()
ax2.plot(x, y1, label='y1')  # 添加标签
ax2.plot(x, y2, label='y2')  # 添加标签
ax2.plot(x, y3, label='y3')  # 添加标签
ax2.legend()  # 显示图例
plt.show()  # 显示图像

x = [1, 2, 3, 4, 5]
y1 = [1, 2, 3, 4, 5]
y2 = [0, 0, 0, 0, 0]
y3 = [-1, -2, -3, -4, -5]

fig, axs = plt.subplots(3, 1, figsize=(8, 6))

axs[0].plot(x, y1)
axs[0].set_title('y1 vs x')

axs[1].plot(x, y2)
axs[1].set_title('y2 vs x')

axs[2].plot(x, y3)
axs[2].set_title('y3 vs x')

plt.tight_layout()
plt.show()

import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(8, 6))

x = [1, 2, 3, 4, 5]
y1 = [1, 2, 3, 4, 5]
y2 = [0, 0, 0, 0, 0]
y3 = [-1, -2, -3, -4, -5]
y4 = [2, 4, 6, 8, 10]
y5 = [3, 6, 9, 12, 15]


ax.plot(x, y1, color='#7CB5EC', label='y1')
ax.plot(x, y2, color='#F7A35C', label='y2')
ax.plot(x, y3, color='#A2A2D0', label='y3')
ax.plot(x, y4, color='#F6675D', label='y4')
ax.plot(x, y5, color='#47ADC7', label='y5')

ax.legend()
plt.show()

import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(8, 6))

ax.plot(x, y1, linestyle='-', label='y1')
ax.plot(x, y2, linestyle='--', label='y2')
ax.plot(x, y3, linestyle='-.', label='y3')
ax.plot(x, y4, linestyle=':', label='y4')
ax.plot(x, y5, linestyle=' ', label='y5')

ax.legend()
plt.show()

fig, ax = plt.subplots(figsize=(8, 6))

ax.plot(x, y1, linewidth=0.5, label='y1')
ax.plot(x, y2, linewidth=1, label='y2')
ax.plot(x, y3, linewidth=1.5, label='y3')
ax.plot(x, y4, linewidth=2, label='y4')

ax.legend()
plt.show()