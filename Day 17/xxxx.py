import math, random
import matplotlib.pyplot as plt


def drawPlot(ax):
    xs = [i / 100 for i in range(1500)]         # 1500个点的横坐标，间隔0.01
    ys = [10*math.sin(x) for x in xs]       # 对应曲线y=10*sin(x)上的1500个点的y坐标
    ax.plot(xs, ys, "red", label="Beijing")
    # 画曲线y=10*sin(x),plot将点从左到右连接起来,看起来是曲线图，实际上是折线图
    ys = list(range(-18, 18))
    random.shuffle(ys)                          # 将-18~17的列表打乱
    ax.scatter(range(16), ys[:16], c="blue")    # 画散点,横坐标0,1,2...15,纵坐标随机
    ax.plot(range(16), ys[:16], "blue", label="Shanghai")   # 画折线
    ax.legend()                                 # 显示右上角的各条折线说明
    ax.set_xticks(range(16))                    # x轴在坐标0,1...15处加刻度
    ax.set_xticklabels(range(16))               # 指定x轴每个刻度下方显示的文字

ax = plt.figure(figsize=(10, 4), dpi=100).add_subplot()    # 图像长度和清晰度
drawPlot(ax)
plt.show()
