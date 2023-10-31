# 郭鑫 20222146060 数据科学与大数据技术
def z_h(n):
    a = 0
    f = list(n)
    b = ''.join(f[-2:])
    m = ''.join(f[:-2])
    m = int(m)
    if "lb" == b:
        a = 0.453 * m
    elif'kg' == b:
        a = 2.204 * m
    return a


x = input()
print(z_h(x))
