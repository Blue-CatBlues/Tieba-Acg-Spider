import numpy as np
array_1d = np.arange(12)
print("原始一维数组:", array_1d)
array_2d = array_1d.reshape((3,4))
print("重塑后的二维数组:\n", array_2d)

arr2=np.array(range(10))
print(arr2)
arr2=arr2.reshape((5,2))
print(arr2)
np.resize(arr2,(1,15))
#np.resize(arr2,(1,15))
np.resize(arr2,(3,4))

print(arr2.dtype)
arr3=arr2.astype(float)
print(arr3.dtype)
arr2.astype(dtype=np.float16)

# arr3 =np.array ([[1,2], [3, 4],[s, 6]])
# arr3.flatten()
# arr3.flatten('F')
arr3 = np.array([[1,2], [3,4], [5,6]])
flattened_row = arr3.flatten()
print("按行扁平化的数组:", flattened_row)

data =np.arange(15).reshape(3, 5)
print (data)
print (np.transpose(data))

print(np.swapaxes(data,0,1))

a =np.arange(24).reshape(2,3,4)
print(a)
a =np.arange(24).reshape(2,3,4)
print(a)