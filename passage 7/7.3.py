# 郭鑫 20222146060 数据科学与大数据技术
import csv
data = [["党组织", "平均参与度", "人均积分"], ["贾汪校区党委", "100.00%", 40],
        ["敬文书院党总", "100.00%", 42], ["化学与材料科学学院党委", "99.76%", 36],
        ["科文学院党委", "99.14%", 25], ["国际学院党总", "97.75%", 49],
        ["马克思主义学院", "97.62%", 37], ["传媒与影视学院", "97.56%", 43],
        ["商学院党委", "95.37%", 22], ["图书馆党总支", "92.35%", 40],
        ["生命科学学院", "89.73%", 25], ["继续教育学院党总支", "89.29%", 41]]

with open("学习强国学习平台使用情况.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(data)
with open("学习强国学习平台使用情况.csv", "r") as f:
    reader = csv.reader(f)
    t = 0
    total_score = 0
    count = 0
    for x in reader:
        if x[0] == "商学院党委":
            t += float(x[1].strip('%'))
            total_score += int(x[2])
            count += 1

avg_can_yu = t / count
avg_score = total_score / count

print("商学院党总支的平均参与度：{:.2f}%".format(avg_can_yu))
print("商学院党总支的人均积分：{:.2f}".format(avg_score))
