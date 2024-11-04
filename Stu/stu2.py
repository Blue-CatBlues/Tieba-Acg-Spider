from itertools import permutations

# 生成包含 1、2、3 的所有排列
perms = permutations("123456789")

# 遍历迭代器中的所有排列
for perm in perms:
    print(perm)
