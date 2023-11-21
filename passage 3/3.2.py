# 郭鑫 20222146060 数据科学与大数据技术
import math
a = int(input("请输入三角形的第一条边："))
b = int(input("请输入三角形的第二条边："))
c = int(input("请输入三角形的第三条边："))
if a + b > c and a + c > b and b + c > a:
    print("三角形周长：{0}".format(a + b + c))
    p = (a + b + c) / 2
    area = math.sqrt(p * (p - a) * (p - b) * (p - c))
    print("三角形面积：{0}".format(area))
else:
    print("输入的边长不构成三角形！")
