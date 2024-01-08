# 郭鑫 20222146060 数据科学与大数据技术
try:
    a = int(input("请输入a的值: "))
    b = int(input("请输入b的值: "))
    s = a + b
    x = a + c
    print("a 和 b 的和为:", x)
except NameError as e:
    print("发生了 NameError 异常:", e)
