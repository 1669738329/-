# 郭鑫 20222146060 数据科学与大数据技术班
print("请输入《中国必胜》藏头诗: ")
a = input()
b = input()
c = input()
d = input()
shi = a + b + c + d
print("《中国必胜》藏头句为: ")
for x in range(4):
    x *= len(a)
    print(shi[0+x])
