# 郭鑫 2222146060 数据科学与大数据技术
# 回文数
def f(x):
    x = str(x)
    a = [n for n in x]
    return a


count = 0
for i in range(1000, 10000):
    # x1 = i // 1000
    # x2 = (i % 1000) // 100
    # x3 = (i % 100) // 10
    # x4 = i % 10
    if f(i)[0] == f(i)[3] and f(i)[1] == f(i)[2]:
        count += 1
        print(i, end='\t')
        if count % 10 == 0:
            print()
