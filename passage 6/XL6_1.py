# 郭鑫 20222146060 数据科学与大数据技术
class Date:
    def __init__(self, year, month, day):
        self.__year = year
        self.__month = month
        self.__day = day

    def get_year(self):
        return self.__year

    def get_month(self):
        return self.__month

    def get_day(self):
        return self.__day

    def set_year(self, year):
        self.__year = year

    def set_month(self, month):
        self.__month = month

    def set_day(self, day):
        self.__day = day

    def f(self):
        print("{0}年{1}月{2}日".format(self.__year, self.__month, self.__day))


if __name__ == "__main__":
    a = Date(2023, 11, 20)
    print(a.get_year())
    print(a.get_month())
    print(a.get_day())
    a.f()
    a.set_year(2024)
    a.set_month(1)
    a.set_day(10)
    a.f()
