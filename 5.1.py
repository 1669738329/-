# 郭鑫 20222146060 数据科学与大数据技术
import math
import random


def su_shu(x):
    for m in range(2, int(math.sqrt(x))):
        if x % m == 0:
            return 0
    return 1


n = random.randint(1, 1000)
a = [x for x in range(1, n) if su_shu(x)]
count = 0
for i in a:
    if n - i in a:
        count += 1
        print("{0}+{1}={2}".format(n - i, i, n))
print("给定的数是{0},有以上{1}种组合".format(n, count))
