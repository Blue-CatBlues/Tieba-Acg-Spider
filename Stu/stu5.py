# 632307110105 刘烨
votes = {}
while True:
    name = input("Enter your name: ")
    if name == "":
        break
    vote = int(input("Enter your vote: "))
    votes[name] = vote

# 把字典转化为带元组的列表
sorted_votes = list(votes.items())
# 匿名函数接收到每个元组，返回元组的第二个值
sorted_votes = sorted(sorted_votes, key=lambda item: item[1], reverse=True)

for name, vote in sorted_votes:
    print(f"{name}: {vote}")
