# 郭鑫 20222146060 数据可与大数据技术班
import math
a = float(input("请输入一条直角边: "))
b = float(input("请输入另一条直角边: "))
c = (math.sqrt(a * a + b * b))
print("直角边分别为:{0} 和 {1}\n斜边长为:{2} ".format(a, b, c))
