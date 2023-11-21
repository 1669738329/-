# 郭鑫 20222146060 数据科学与大数据技术
sum, a, b = 0.0, 2, 1
for i in range(1, 21):
    sum += a / b
    c = a
    a = a + b
    b = c
print("sum = {:.2f}".format(sum))
