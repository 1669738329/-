# 郭鑫 20222146060 数据科学与大数据技术班
print("Python超市收银系统")
commodity = input("商品名称: ")
monovalent = float(input("商品单价: "))
quantity = float(input("数量: "))
price = monovalent * quantity
print("应付金额:{:.2f}".format(price))
pay = float(input("实收: "))
print("Python超市购物小票")
print("商品名称\t单价 \t数量")
print("{0}\t\t{1} \t{2}".format(commodity, monovalent, quantity))
print("应付:{:.2f}".format(price))
print("实收:{0}".format(pay))
print("找零:{:.1f}".format(pay-price))
