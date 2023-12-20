# 郭鑫 20222146060 数据科学与大数据技术
s = 0
for i in range(1000, 10000):
    a = i // 1000
    b = i % 1000 // 100
    c = i % 100 // 10
    d = i % 10
    if a == d and b == c:
        s = s + 1
        with open("palindrome.txt", "a") as f:
            f.write(str(i)+'\t')
            if s % 10 == 0:
                f.write('\n')
