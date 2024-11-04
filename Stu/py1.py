import turtle as t

t.fillcolor("red")
t.begin_fill()
t.fd(180)  # 向当前方向前进180像素
t.lt(90)   # 左转90度
t.fd(180)
t.goto(0, 0)  # 返回起点
t.end_fill()

t.fillcolor("yellow")
t.begin_fill()
t.fd(180)
t.rt(90)   # 右转90度
t.fd(180)
t.goto(0, 0)  # 返回起点
t.end_fill()


t.hideturtle()  # 隐藏画笔
