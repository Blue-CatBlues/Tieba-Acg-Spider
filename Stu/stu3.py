# 632307110105 刘烨
numbers = []
print("请输入一组数字（用空格分隔），按回车键结束：")
input_numbers = input().split()
for num in input_numbers:
    numbers.append(float(num))
# 计算平均值
mean = sum(numbers) / len(numbers)
# 计算方差
variance = sum((x - mean) ** 2 for x in numbers) / len(numbers)
# 计算中位数
sorted_numbers = sorted(numbers)
n = len(sorted_numbers)
if n % 2 == 0:
    median = (sorted_numbers[n//2 - 1] + sorted_numbers[n//2]) / 2
else:
    median = sorted_numbers[n//2]

print(f"平均值: {mean}")
print(f"方差: {variance}")
print(f"中位数: {median}")
