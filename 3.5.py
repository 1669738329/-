# 郭鑫 20222146060 数据科学与大数据技术
import random
import time
n = random.randint(1,100)
start_time = time.time()
x = int(input("请输入一个1~100的整数\n"))
while x != n:
    if x > n:
        print("大了！")
    else:
        print("小了！")
    x = int(input("请输入一个1~100的整数\n"))
print("猜对了！")
end_time = time.time()
print("用时:{:.1f}秒".format(end_time - start_time))
