from decimal import Decimal, ROUND_HALF_EVEN

while True:
    try:
        # 输入四个浮点数
        numbers = input("请输入四个浮点数（用空格分隔）：").split()

        # 将输入的字符串转换为浮点数
        numbers = [float(num) for num in numbers]

        # 检查是否输入了四个数
        if len(numbers) != 4:
            print("请输入恰好四个浮点数。")
            continue

        # 计算平均值
        average = sum(numbers) / 4

        # 使用Decimal进行四舍六入五凑偶的舍入
        average = Decimal(average).quantize(Decimal('0.00'), rounding=ROUND_HALF_EVEN)

        # 输出平均值，保留两位小数
        print(f"平均值：{average}")

    except ValueError:
        print("输入无效，请输入有效的浮点数。")
