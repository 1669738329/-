# 郭鑫 20222146060 数据科学与大数据技术
count = 0
a = '33'
for i in range(3, 1000, 10):
    count += 1
    if i % 3 == 0:
        b = str(i)
        if a in b:
            print("&{0}".format(b), end=' ')
        else:
            print(i, end=' ')
    else:
        print("{0}*".format(i), end=' ')
    if count % 10 == 0:
        print()
