# 郭鑫 20222146060 数据科学与大数据技术
import random
poet_writer = {"锄禾": "李绅", "九月九日忆山东兄弟": "王维","咏鹅": "骆宾王",
               "秋浦歌": "李白", "竹石": "郑燮", "石灰吟": "于谦", "示儿": "陆游"}
poetry = list(poet_writer.values())
poet = list(poet_writer.keys())
p = random.choice(poet)
print("{0}的作者是谁".format(p))
right = poet_writer[p]
poetry.remove(right)
xuan_xiang = ["A", "B", "C", "D"]
answer = [right]
for i in range(3):
    answer.append(random.choice(poetry))
random.shuffle(answer)
dict_1 = dict(zip(xuan_xiang,answer))
for xuan_xiang,answer in dict_1.items():
    print(xuan_xiang,answer)
shu_ru = input("请输入答案：")
if dict_1[shu_ru] == right:
    print("正确！")
else:
    print("错误！")
