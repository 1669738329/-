# 郭鑫 20222146060 数据科学与大数据技术
class Rational:
    def __init__(self, fen_zi, fen_mu):
        self.fen_zi = fen_zi
        if b == 0:
            print("分母不能为0！")
        else:
            self.fen_mu = fen_mu
        self.yue_fen()

    def __str__(self):
        return "({0}/{1})".format(self.fen_zi, self.fen_mu)

    # 辗转相除法
    def qiu_yu(self):
        m = self.fen_zi
        n = self.fen_mu
        while m % n != 0:
            m, n = n, m % n
        return n

    def yue_fen(self):
        yu_shu = self.qiu_yu()
        self.fen_zi //= yu_shu
        self.fen_mu //= yu_shu

    def __add__(self, other):
        return Rational(self.fen_zi * other.fen_mu + other.fen_zi * self.fen_mu,
                        self.fen_mu * other.fen_mu)

    def __sub__(self, other):
        return Rational(self.fen_zi * other.fen_mu - other.fen_zi * self.fen_mu,
                        self.fen_mu * other.fen_mu)

    def __mul__(self, other):
        return Rational(self.fen_zi * other.fen_zi, self.fen_mu * other.fen_mu)

    def __truediv__(self, other):
        return Rational(self.fen_zi * other.fen_mu, self.fen_mu * other.fen_zi)

    def __lt__(self, other):
        z = (self.fen_mu * other.fen_mu)
        x = self.fen_zi * z
        y = other.fen_zi * z
        if x < y:
            return True
        else:
            return False

    def __le__(self, other):
        z = (self.fen_mu * other.fen_mu)
        x = self.fen_zi * z
        y = other.fen_zi * z
        if x <= y:
            return True
        else:
            return False

    def __gt__(self, other):
        z = (self.fen_mu * other.fen_mu)
        x = self.fen_zi * z
        y = other.fen_zi * z
        if x > y:
            return True
        else:
            return False

    def __ge__(self, other):
        z = (self.fen_mu * other.fen_mu)
        x = self.fen_zi * z
        y = other.fen_zi * z
        if x >= y:
            return True
        else:
            return False


a = Rational(1, 12)
b = Rational(3, 6)
print("{0} + {1} = {2}".format(a, b, a+b))
print("{0} - {1} = {2}".format(a, b, a-b))
print("{0} * {1} = {2}".format(a, b, a*b))
print("{0} / {1} = {2}".format(a, b, a/b))
print("{0} <= {1} = {2}".format(a, b, a <= b))
print("{0} > {1} = {2}".format(a, b, a > b))
