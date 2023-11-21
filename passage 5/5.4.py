# 郭鑫 20222146060 数据科学与大数据技术
def fibo(x):
    if x <= 2:
        n = 1
        return n
    return fibo(x - 1) + fibo(x - 2)


for i in range(1, 21):
    print(i, fibo(i))
