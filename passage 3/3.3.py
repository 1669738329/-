# 郭鑫 20222146060 数据科学与大数据技术
chen_ji = []
yu_wen, math, english, science = input("请输入语文、数学、英语、科学的成绩：").split(" ")
chen_ji.append(yu_wen)
chen_ji.append(math)
chen_ji.append(english)
chen_ji.append(science)
if int(yu_wen + math + english + science) >= 380:
    for i in range(4):
        if int(chen_ji[i]) >= 95:
            if i == 3:
                print("该生是优等生！")
        else:
            print("该生不是优等生！")
            break
else:
    print("该生不是优等生！")
