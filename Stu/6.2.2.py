print("---------------------常用属性----------------------------")
import numpy as np
l = [1, 2, 3,4,5,6]
data = np.array(l)
print(data)
print("维度个数",data.ndim)
print("各维度大小",data.shape)
print("数据类型",data.dtype)
print("数组元素总个数",data.size)