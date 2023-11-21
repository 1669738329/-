# 郭鑫 20222146060 数据科学与大数据技术班
weight = float(input("请输入体重："))
height = float(input("请输入身高："))
age = int(input("请输入年龄："))
a = 655 + (9.6 * weight) + (1.7 * height) - (4.7 * age)
print("女性的基础代谢为:{0}".format(a))
