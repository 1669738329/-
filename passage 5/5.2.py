# 郭鑫 20222146060 数据科学与大数据技术
def change(str1):
    a = []
    for i in str1:
        if 'a' <= i <= 'z':
            a.append(chr(ord(i)-32))
        elif 'A' <= i <= 'Z':
            a.append(chr(ord(i)+32))
    a = ''.join(a)
    return a


x = input("请输入字符串：")
print("大小写转换后{}".format(change(x)))
