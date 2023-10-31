# 郭鑫 20222146060 数据科学与大数据技术
def digit(num, k):
    a = [x for x in str(num)]
    return a[k-1]


y = int(input("请输入数字："))
z = int(input("请输入位数："))
print("输入{0},第{1}位为{2}".format(y, z, digit(y, z)))
