# 郭鑫 20222146060 数据科学与大数据技术
def f(n):
    count = 0
    a = []
    for i in range(1, n):
        if n % i == 0:
            count += i
            a.append(i)
    if count == n:
        return 1, a
    else:
        return 0


for x in range(1, 1000):
    if f(x):
        print("sum({0}) = {1}".format(f(x)[1], x))
