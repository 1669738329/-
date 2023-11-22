# 郭鑫 20222146060 数据科学与大数据技术
import math


class San:
    def __init__(self, a, b, c):
        if a + b > c and a + c > b and b + c > a:
            self.__a = a
            self.__b = b
            self.__c = c
        else:
            print("{},{},{}不能组成三角形！".format(self.__a, self.__b, self.__c))

    def area(self):
        s = (self.__a + self.__b + self.__c) / 2
        print("三角形面积:{}".format(math.sqrt(s * (s - self.__a) * (s - self.__b) * (s - self.__c))))

    def circumference(self):
        print("三角形周长:{}".format(self.__a+self.__b+self.__c))


class Square:
    def __init__(self, bian):
        self.__bian = bian

    def area(self):
        print("正方形面积:{}".format(self.__bian * self.__bian))

    def circumference(self):
        print("正方形周长:{}".format(4 * self.__bian))


class Circle(object):
    def __init__(self, radius):
        self.__radius = radius

    def area(self):
        print("圆面积:{:.2f}".format(math.pi * self.__radius * self.__radius))

    def circumference(self):
        print("圆周长:{:.2f}".format(2 * math.pi * self.__radius))


x = San(3, 4, 5)
x.area()
x.circumference()
y = Square(3)
y.area()
y.circumference()
z = Circle(3)
z.area()
z.circumference()
