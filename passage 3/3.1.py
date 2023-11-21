# 郭鑫 20222146060 数据科学与大数据技术
year = int(input("请输入年份："))
if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print("{0}是闰年".format(year))
else:
    print("{0}不是闰年".format(year))
# 原来GitHub这么好玩
