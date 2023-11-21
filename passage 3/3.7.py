# 郭鑫 20222146060 数据科学与大数据技术
print("Pytnon超市收银收银系统：")
products_number = int(input("商品个数："))
sum, product_name, product_price, product_number = 0.0, [], [], []
print("商品名称\t单价\t\t数量")
for i in range(products_number):
    name, price, number = input().split(" ")
    product_name.append(name)
    product_price.append(float(price))
    product_number.append(float(number))
    sum += product_price[i] * product_number[i]
print("应付金额：{:.2f}".format(sum))
pay = float(input("实收："))
print("Python超市购物小票")
print("共购买{0}件商品".format(products_number))
print("商品名称\t单价\t\t数量")
for i in range(products_number):
    print("{0}\t\t{1}\t{2}".format(product_name[i], product_price[i], product_number[i]))
print("应付:{0:.2f}\n实收:{1:.2f}\n找零:{2:.2f}".format(sum, pay, pay - sum))
