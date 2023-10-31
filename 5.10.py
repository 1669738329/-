# 郭鑫 20222146060 数据科学与大数据技术
def f(n):
    if n == -1:
        return ""
    else:
        return str1[n] + f(n -1)
str1 = input()
print(f(len(str1)-1))