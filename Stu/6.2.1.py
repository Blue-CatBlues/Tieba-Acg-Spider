# 632307110105 刘烨
import numpy as np
# 创建数组array
print("------------创建一二三维数组和数组的类型转换--------------")
arr1 = np.array([1, 2, 3])
print(arr1)
# 整数数组转换为 → 浮点数数组
arr2 = arr1.astype(float)
print(arr2)
# 浮点数数组 → 整数数组
arr3 = arr2.astype(int)
print(arr3)
# 创建一维数组
arr1 = np.ones(3)
print(arr1)
# 创建二维数组
arr2 = np.ones((1, 3))
print(arr2)
# 创建三维数组
arr3 = np.ones((1, 1, 3))
print(arr3)
# 输出数组形状
print(arr1.shape)
print(arr2.shape)
print(arr3.shape)
print("--------------------改变数组形状----------------------")
# 创建一个范围为10的数组并改变形状
arr2 = np.arange(10).reshape(2, 5)
print(arr2)
# 修改数组的形状
arr1 = arr2.reshape(-1)
print(arr1)
# 创建一维数组
arr1 = np.array([1, 2, 3])
print(arr1)
# 创建二维数组
arr2 = np.array([[1, 2, 3]])
print(arr2)
# 创建二维数组（列矩阵）
arr3 = np.array([[1], [2], [3]])
print(arr3)
print("-----------------ones和zeros函数----------------------")
# 创建一个长度为3的零数组
arr1 = np.zeros(3)
print(arr1)
# 创建一个元素为1的(1,3)数组
arr2 = np.ones((1,3))
print(arr2)
print("------------------------linspace函数----------------------------")
arr1 = np.linspace(0, 10, 3)
arr2 = np.linspace(0, 10, 3, endpoint=False)
print(arr1)
print(arr2)
print("------------------empty函数-----------------------------")
arr1 = np.empty((3, 4))
arr2 = np.empty((6,),dtype=list)
print(arr1)
print(arr2)