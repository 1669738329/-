# 郭鑫 20222146060 数据科学与大数据技术
import struct


def w():
    n = int(input("学生数："))
    for i in range(n):
        a, b, c = input("请输入学号，姓名，成绩：").split(" ")
        id = b"a"
        name = "b".encode()
        score = float(c)
        student = struct.pack('12s8sf', id, name, score)
        with open("student.bin", "wb") as f:
            f.write(student)
        with open("student.bin", "rb") as f:
            size = struct.calcsize("12s8sf")
            stu = f.read(size)
            stu = struct.unpack("12s8sf", stu)
            print(stu)
            id, name, score = stu
            print(id.decode(), '', name.decode(), '', score)


w()