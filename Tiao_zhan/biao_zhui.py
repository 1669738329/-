import time
s = time.time()


def check_number(n):
    if n > 10:
        # 将数字转换为字符串，然后转换为列表，这样我们就可以逐个访问每个数字
        digits = list(str(n))
        for x in range(1, n):
            num = sum(int(digit) ** x for digit in digits)
            # 计算各位数字的x次方之和
            if num == n:
                return n, x
            elif num > n or len(digits) >= num:
                return n, -1
            else:
                continue


for i in range(11, 10000):
    num, x = check_number(i)
    if x != -1:
        print([num, x])
e = time.time()
print(e-s)
