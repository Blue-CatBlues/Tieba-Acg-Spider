import numpy as np
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