try:
    a = int(input("请输入a的值: "))
    b = int(input("请输入b的值: "))
    x = a + b
    print("a 和 b 的和为:", x)
except ValueError as e:
    print("发生了 ValueError 异常:", e)
