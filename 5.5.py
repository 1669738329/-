# 郭鑫 20222146060 数据科学与大数据技术
def cacluate(*x):
    count = 0
    a = sum(x) / len(x)
    for i in x:
        if i < a:
            count += 1
    return a, count


print(cacluate(1, 2, 3, 4, 5))
