# 郭鑫 20222146060 数据科学与大数据技术
import XL6_1


class CCPM:
    def __init__(self, name, sex, id, time, money):
        self.__name = name
        self.__sex = sex
        self.__id = id
        self.__time = time
        self.__money = money

    def get(self):
        return self.__name, self.__sex, self.__id, self.__time, self.__money

    def set(self, name, sex, id, time, money):
        self.__name = name
        self.__sex = sex
        self.__id = id
        self.__time = time
        self.__money = money

    def f(self):
        print('''姓名:{0}\n性别:{1}\n身份证号:{2}\n入党时间:{3}\n党费:{4}/月
        '''.format(self.__name, self.__sex, self.__id, self.__time, self.__money))


day = XL6_1.Date(2023, 11, 20)
a = CCPM("张三", "男", "12346", "day", 20)
a.f()
