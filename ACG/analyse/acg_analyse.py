import pandas as pd

# 读取 Excel 文件
df = pd.read_excel("D:\\AAAPycharmProjects\\ACG\\acg_output.xlsx")

# 按照关注人数排序，并输出前后20个吧的名称
df_sorted_by_member = df.sort_values(by='关注人数', ascending=False)
top_20_members = df_sorted_by_member.head(20)
bottom_20_members = df_sorted_by_member.tail(20)

print("前20个吧（按关注人数）：")
print(top_20_members[['贴吧', '关注人数']])

print("\n后20个吧（按关注人数）：")
print(bottom_20_members[['贴吧', '关注人数']])

# 按照帖子数排序，并输出前后20个吧的名称
df_sorted_by_comment = df.sort_values(by='帖子数', ascending=False)
top_20_comments = df_sorted_by_comment.head(20)
bottom_20_comments = df_sorted_by_comment.tail(20)

print("\n前20个吧（按帖子数）：")
print(top_20_comments[['贴吧', '帖子数']])

print("\n后20个吧（按帖子数）：")
print(bottom_20_comments[['贴吧', '帖子数']])
