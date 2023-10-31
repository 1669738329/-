# 郭鑫 20222146060 数据科学与大数据技术
import random


def game(x):
    if 0 <= x < 0.08:
        return '一'
    elif 0.08 <= x < 0.3:
        return '二'
    else:
        return '三'


n = random.random()
print("你抽到了{0:.2f}，并获得了{1}等奖".format(n, game(n)))
