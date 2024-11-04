import numpy as np
from datetime import datetime


def load_data(filename, use_cols):

    # 读取列名，即第一行数据
    with open(filename, 'r') as f:
        col_names_str = f.readline()[:-1]  # 读取第一行并去掉末尾的换行符
    print("col_names_str", col_names_str)
    # 将字符串拆分，并组成列表
    col_name_lst = col_names_str.split(',')  # 将列名字符串按逗号分隔成列表
    print("col_name_lst", col_name_lst)
    # 获取相应列名的索引号
    use_col_index_lst = [col_name_lst.index(use_col_name) for use_col_name in use_cols]  # 找到需要读取的列的索引

    # 读取数据
    data_array = np.loadtxt(filename,
                            delimiter=',',  # 指定分隔符为逗号
                            skiprows=1,  # 跳过第一行（列名）
                            dtype=str,  # 数据类型为字符串
                            usecols=use_col_index_lst)  # 只读取指定列的数据

    return data_array  # 返回读取的数据数组


def process_date(data_array):

    # 将日期字符串转换为列表
    enddate_lst = data_array[:, 0].tolist()  # 提取第一列（日期列）并转换为列表

    # 将日期字符串格式统一，即 'MM/DD/YYYY'
    enddate_lst = [enddate.replace('/', '-') for enddate in enddate_lst]  # 将日期中的斜杠替换为短横线

    # 将日期字符串转换成日期对象
    date_lst = [datetime.strptime(enddate, "%m-%d-%Y") for enddate in enddate_lst]  # 将字符串转换为日期对象

    # 构造年份-月份列表
    month_lst = ['{}-{:02d}'.format(date_obj.year, date_obj.month) for date_obj in date_lst]  # 格式化为 'YYYY-MM'

    # 将年份-月份列表转换为数组并替换原数组中的日期列
    month_array = np.array(month_lst)  # 转换为数组
    data_array[:, 0] = month_array  # 替换原数组中的日期列

    return data_array  # 返回处理后的数据数组


def get_month_stats(data_array):

    # 获取唯一的月份列表
    months = np.unique(data_array[:, 0])  # 获取唯一的月份

    # 统计每月的投票数据
    for month in months:
        # 根据月份过滤数据
        filtered_data = data_array[data_array[:, 0] == month]  # 过滤出当前月份的数据

        # 获取投票数据，字符串数组转换为数值型数组
        try:
            filtered_poll_data = filtered_data[:, 1:].astype(float)  # 转换为浮点数数组
        except ValueError:
            # 遇到不能转换为数值的字符串，跳过循环
            continue

        # 按列方向求和
        result = np.sum(filtered_poll_data, axis=0)  # 计算每列的和
        print('月份: {}, Clinton 票数: {}, Trump 票数: {}'.format(month, result[0], result[1]))  # 打印结果


def main():

    # 数据文件路径
    filename = 'D:\\AAAPycharmProjects\\rawpoll\\presidential_polls.csv'  # 数据文件的路径

    # 指定需要读取的列
    use_cols = ['enddate', 'rawpoll_clinton', 'rawpoll_trump']  # 需要读取的列名

    # 读取指定列的数据
    data_array = load_data(filename, use_cols)  # 调用 load_data 函数读取数据

    # 处理日期格式数据，转换为 'YYYY-MM' 字符串
    proc_data_array = process_date(data_array)  # 调用 process_date 函数处理日期

    # 统计每月的投票数据
    get_month_stats(proc_data_array)  # 调用 get_month_stats 函数统计数据


if __name__ == "__main__":
    main()  # 运行主函数
