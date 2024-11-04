# 632307110105 刘烨
import numpy as np
arr1 = np.array([1,2,3,4,5,6,7,8,9,10]) # 列表转为数组
np.array((1,2,3,4,5)) # 元组转为数组
np.arange(10)
arr2 = np.ones((1, 3))
print(arr2)
arr2 = arr1.astype(float)
print(arr2)

arr3 = arr2.astype(int)
print(arr3)

arr1 = np.ones(3)
print(arr1)
arr2 = np.ones((1,3))
print(arr2)
arr3 = np.ones((1,1,3))
print(arr3)

arr1 = np.arange(10).reshape(2,5)
print(arr1)

# (-1)是改为向量 ，（1，-1）是改为一行的二维数组
arr2 = arr1.reshape(-1)
print(arr2)

arr1 = np.zeros(3)
print(arr1)

arr1 = np.zeros((1,3))
print(arr1)

arr1 = np.full((2,3),3.14)
print(arr1)

arr1 = 3.14*np.ones((2,3))
print(arr1)

arr2 = np.random.randint(0,10,(1,15))
print(arr2)

arr1 = 50*np.random.random((1,15)) + 50
print(arr1)

arr3 = np.random.normal(0,1,(2,15))
print(arr3)

arr1 = np.arange(10)
print(arr1[4])
print(arr1[4:5])

arr2 = np.arange(1,21).reshape(4,-1)
print(arr2)

print(arr2[1:3,1:-1])
print(arr2[::3,::2])

cut = arr1[2:8]
print(cut)
cut[0] = 100
print(cut)
print(arr1)

arr1 = np.array([[1,2,3],[4,5,6]])
arr2 = np.array([[1,2,3],[4,5,6]])
arr3 = np.concatenate((arr1,arr2),axis=0)
print(arr3)
arr4 = np.concatenate((arr1,arr2),axis=1)
print(arr4)

arr1,arr2 = np.split(arr4,2)
print(arr1,"\n\n",arr2)
print("////")
arr1,arr2,arr3 = np.split(arr4,3,axis=1)
print(arr1,"\n\n",arr2,"\n\n",arr3)