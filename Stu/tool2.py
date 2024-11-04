from decimal import Decimal, ROUND_HALF_EVEN

# 常量 k 和 i
k = 173
i = 0.003

while True:
    try:
        # 输入电压值 u
        u = float(input("请输入电压值 u："))

        # 计算 b 的值
        b = u / (k * i)

        # 使用 Decimal 进行四舍六入五凑偶的舍入，并转换为科学计数法
        b = Decimal(b).quantize(Decimal('0.00E-3'), rounding=ROUND_HALF_EVEN)

        # 输出 b 的值，保留两位有效数字
        print(f"b 的值：{b} * 10^-3")

    except ValueError:
        print("输入无效，请输入有效的浮点数。")
