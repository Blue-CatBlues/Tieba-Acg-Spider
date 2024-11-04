import pandas as pd

flie = pd.read_excel(r"D:\\AAAPycharmProjects\\ACG\\acg_output.xlsx")
# print(type(flie))
# print(flie.dtypes)
# print(flie.columns)
# print(flie.head(10))
# print(flie[["贴吧", "关注人数"]])

top = flie[flie["关注人数"]>=1000000]
flie["人数/帖子数"] =  flie["帖子数"] / flie['关注人数']

def high():
    print(flie[flie["人数/帖子数"] >= 100])

def low():
    print(flie[flie["人数/帖子数"] <= 5])

import pandas as pd

flie = pd.read_excel(r"D:\\AAAPycharmProjects\\ACG\\acg_output.xlsx")

def high_mem():
    sorted_flie = flie.sort_values("关注人数", ascending=False)
    mem_20 = sorted_flie[["贴吧", "关注人数", "帖子数"]].head(20)
    print("Top 20 by 关注人数:")
    print(mem_20)
    return mem_20

def high_comment():
    sorted_flie = flie.sort_values("帖子数", ascending=False)
    comment_20 = sorted_flie[["贴吧", "关注人数", "帖子数"]].head(20)
    print("Top 20 by 帖子数:")
    print(comment_20)
    return comment_20

def high_hot():
    mem_20 = high_mem()
    comment_20 = high_comment()
    # 指定合并的列
    top = pd.merge(mem_20, comment_20, on=["贴吧", "关注人数", "帖子数"])
    print("关注人数和帖子数都名列前20的贴吧有：")
    print(top)

high_hot()



