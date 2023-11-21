# 郭鑫 20222146060 数据科学与大数据技术
salary = float(input("请输入工资："))
insurance = float(input("请输入五险一金："))
other = float(input("其他专项："))
s = salary - 5000 - insurance - other
if s <= 0:
    a, b = 0, 0
elif s < 3000:
    a, b = 0.03, 0
elif s < 12000:
    a, b = 0.1, 210
elif s < 25000:
    a, b = 0.2, 1410
elif s < 35000:
    a, b = 0.25, 2660
elif s < 55000:
    a, b = 0.3, 4410
elif s < 80000:
    a, b = 0.35, 7160
else:
    a, b = 0.45, 15160
tax = abs(s * a - b)
payroll = salary - tax - insurance
print("个人所得税:{:.2f}".format(tax))
print("实发工资:{:.2f}".format(payroll))
