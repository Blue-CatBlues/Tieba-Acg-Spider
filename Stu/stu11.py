# 632307110105 刘烨
import numpy as np

# # 1
# arr1 = np.arange(15)
# arr2 = arr1[5:11]
# print(arr2)

# # 2
# arr1 = np.arange(20).reshape(4,-1)
# arr1[[0,1]] = arr1[[1,0]]
# arr1[:,[0,1]] = arr1[:,[1,0]]
# print(arr1)

# # 3
# arr1 = np.random.randint(1,10,size=(5,5))
# arr1[arr1 % 2 != 0] = 0
# print(arr1)

# # 4
# arr1 = np.random.randint(1, 51, size=20)
# arr1[arr1 >= 30] = 0
# arr1 = np.argsort(arr1)
# print(arr1[-5:])

# # 5
# arr1 = np.array([[1, 9], [5, 12], [8, 20], [4, 10], [2, 8]])
# distances = np.sqrt(np.sum(np.diff(arr1, axis=0)**2, axis=1))
# end = np.sqrt(np.sum((arr1[-1] - arr1[0])**2))
# # 总周长
# sum = np.sum(distances) + end
# print(sum)

# # 6
# data = np.random.randint(50, 101, size=(10, 6))
# # 2) 水平方向的总和统计及垂直方向上平均值统计
# x_sum = np.sum(data, axis=1)
# y_mean = np.mean(data, axis=0)
# print("水平方向的总和：")
# print(x_sum)
# print("垂直方向的平均值：")
# print(y_mean)
# # 3) 水平方向上的最大值与最小值差值的统计
# x_cha = np.ptp(data, axis=1)
# print("水平方向上的最大值与最小值差值：")
# print(x_cha)
# # 4) 统计数据中数值在90以上的比率
# c90 = np.sum(data > 90)
# total = data.size
# ratio_above_90 = c90 / total
# print("数据中数值在90以上的比率：")
# print(ratio_above_90)

# # 7
# arr1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# x_sum = np.sum(arr1, axis=1)
# print(x_sum)
# y_sum = np.sum(arr1, axis=0)
# print(y_sum)
# xx_sum = np.cumsum(arr1, axis=1)[:, -1]
# print(xx_sum)
# yx_sum = np.cumsum(arr1, axis=0)[:, -1]
# print(yx_sum)
# arr2 = np.sort(arr1, axis=1)
# print(arr2)

# # 8
# arr1 = np.array([[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]])
# arr1_1, arr1_2 = np.hsplit(arr1, 2)
# print(arr1_1, arr1_2)
#
# arr1_a, arr1_b, arr1_c, arr1_d = np.hsplit(arr1, 4)
# print(arr1_a, arr1_b, arr1_c, arr1_d)
#
# arr2 = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
#
# arr2_1,arr2_2,arr2_3 = np.vsplit(arr2, 3)
# print(arr2_1, arr2_2, arr2_3)

# # 9
# arr1 = np.random.randint(0, 101, size=(10, 10))
# print(arr1)
# print(np.max(arr1))
# print(np.min(arr1))

# 10
arr1 = np.arange(1, 25).reshape(6, -1)
print(arr1)
row_0 = arr1[0]
print("第0行的数据元素：")
print(row_0)
row_3 = arr1[:3]
print("前三行的数据元素：")
print(row_3)
a = arr1[1, 2]
print("第1行第2列中的元素：")
print(a)
arr = arr1.T
print("1转置后的数组：")
print(arr)