from scipy.optimize import linprog

# 示例数据
P = [10, 12, 8]  # 销售价格
Y = [100, 80, 120]  # 亩产量
C = [5, 6, 4]  # 种植成本
A = [50, 60, 40]  # 种植面积

# 目标函数系数（负号表示最大化）
c = [-P[i] * Y[i] + C[i] for i in range(len(P))]

# 约束条件
A_eq = [[1, 1, 1]]  # 总面积约束
b_eq = [150]  # 总面积

# 求解
result = linprog(c, A_eq=A_eq, b_eq=b_eq, bounds=(0, None))

print("最优种植方案：", result.x)
print("最大利润：", -result.fun)
