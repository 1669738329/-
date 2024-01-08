# 郭鑫 20222146060 数据科学与大数据技术
class TriangleError(Exception):
    def __init__(self, x="Triangle Error"):
        self.x = x
        super().__init__(self.x)


def san_jiao(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a:
        raise TriangleError("三角形的边长不满足条件")
    else:
        print("三角形的边长满足条件")


try:
    x = float(input("请输入第一条边的长度: "))
    y = float(input("请输入第二条边的长度: "))
    z = float(input("请输入第三条边的长度: "))
    san_jiao(x, y, z)

except TriangleError as e:
    print("发生了 TriangleError 异常:", e)
