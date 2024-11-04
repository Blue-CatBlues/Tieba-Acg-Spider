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
# 创建一个元素为π的(2,3)数组
arr3 = np.full((2,3), 3.14)
print(arr3)
print("--------------------random函数和rand函数------------------------")
arr1 = (100 - 60) * np.random.random((3, 3)) + 60
print(arr1)
# 生成随机整数数组
arr2 = np.random.randint(10, 100, (1, 15))
print(arr2)
# 标准正态分布的数组
arr3 = np.random.normal(0, 1, (2, 3))
print(arr3)
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
print("---------------------常用属性----------------------------")
l = [1, 2, 3]
data = np.array(l)
print(data)
print("维度个数",data.ndim)
print("各维度大小",data.shape)
print("数据类型",data.dtype)
print("数组元素总个数",data.size)
print("-----------------------数组降维-----------------------------")
array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
f_array = array.flatten()
print(f_array)
print("-------------------查找数组元素--------------------------")
arr1 = np.arange(10)
print(arr1[4])
print(arr1[1:4])
print(arr1[:5])
print(arr1[5:])
print(arr1[-5:])
print(arr1[:-2])
print(arr1[::2])
print(arr1[::-2])
arr2 = np.arange(1, 21).reshape(4, 5)
print(arr2)

print("----------------------矩阵切片-------------------------------")
# 矩阵切片初体验
print(arr2[1:3, 1:-1])
print(arr2[::3, ::2])
arr = np.arange(10)
print(arr)  # 输出: [0 1 2 3 4 5 6 7 8 9]
cut = arr[:3]
print(cut)  # 输出: [0 1 2]
cut[0] = 100
print(cut)  # 输出: [100 1 2]
print(arr)  # 输出: [100 1 2 3 4 5 6 7 8 9]
# 创建一个包含0到9的数组
arr1 = np.arange(10)
print(arr1)  # 输出: [0 1 2 3 4 5 6 7 8 9]
arr2 = arr1.copy()
print(arr2)  # 输出: [0 1 2 3 4 5 6 7 8 9]
arr2[0] = 100
print(arr2)  # 输出: [100 1 2 3 4 5 6 7 8 9]
print(arr1)  # 输出: [0 1 2 3 4 5 6 7 8 9]
print("-------------------数组拼接和分裂----------------------")
# 创建数组 1
arr1 = np.array([[1, 2, 3], [4, 5, 6]])
print(arr1)
arr2 = np.array([[7, 8, 9], [10, 11, 12]])
print(arr2)
# 按第一个维度(行)拼接
arr3 = np.concatenate([arr1, arr2], axis=0)
print(arr3)
# 按第二个维度(列)拼接
arr4 = np.concatenate([arr1, arr2], axis=1)
print(arr4)
# 创建矩阵
arr = np.arange(1, 9).reshape(2, 4)
print(arr)

# 按第一个维度(行)分裂
arr1, arr2 = np.split(arr, [1])
print(arr1, '\n\n', arr2)
arr1, arr2, arr3 = np.split(arr, [1, 3], axis=1)
print(arr1, '\n\n', arr2, '\n\n', arr3)
print("-------------------numpy常用函数----------------------")
arr_v = np.array([-10, 0, 10])
print('原数组是:', arr_v)
# 计算绝对值
abs_v = np.abs(arr_v)
print('绝对值是:', abs_v)
# 创建角度数组
theta = np.arange(3) * np.pi / 2
print('原数组是:', theta)
# 计算三角函数值
sin_v = np.sin(theta)
cos_v = np.cos(theta)
tan_v = np.tan(theta)
print('正弦值是:', sin_v)

print('余弦值是:', cos_v)
print('正切值是:', tan_v)
x = np.array([1, 10, 100, 1000])
print('x        =', x)
print('ln(x)    =', np.log(x))
print('log2(x)  =', np.log(x) / np.log(2))
print('log10(x) =', np.log(x) / np.log(10))
print("-------------------------------------------------------------------")
arr2 = np.arange(1, 17).reshape(4, -1)
arr3 = np.linalg.inv(arr2)
print(arr3)
print(arr2*arr3)




