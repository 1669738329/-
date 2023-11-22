# 郭鑫 20222146060 数据科学与大数据技术
class Person:
    def __init__(self, name, sex, age):
        self.__name = name
        self.__sex = sex
        self.__age = age

    def f(self):
        print("姓名:{0}\n性别:{1}\n年龄:{2}".format(self.__name, self.__sex, self.__age))


class Student(Person):
    def __init__(self, name, sex, age, xh, score):
        Person.__init__(self, name, sex, age)
        self.__xh = xh
        self.__score = score

    def f(self):
        Person.f(self)
        print("学号:{0}\n分数:{1}".format(self.__xh, self.__score))


class Teacher(Person):
    def __init__(self, name, sex, age, department, gh, salary):
        Person.__init__(self, name, sex, age)
        self.__department = department
        self.__gh = gh
        self.__salary = salary

    def f(self):
        Person.f(self)
        print("院系:{0}\n工号:{1}\n工资:{2}".format(self.__department, self.__gh, self.__salary))


a = Teacher("张三", "男", 25, "生工", 123456, 5000)
a.f()






#b = Student("郭鑫", "男", 20, 20222146060, 90)
#b.f()
