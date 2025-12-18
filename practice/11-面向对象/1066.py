# 题目描述
# 设计一个一元二次方程类QE。QE类通过构造函数初始化方程的系数，同时具有getA、getB、getC方法取每个系数的值，
# 也可以通过getD计算判别式的值，getRoot1()和 getRoot2()的方法分别计算方程式的两个根，
# 如果判别式为负时，这两个方法抛出异常ValueError。
# 测试程序输入一个一元二次方程的系数 a、b和c，构建QE类对象，通过getA、getB、getC方法输出每个系数，然后输出这个方程的判别式。
# 如果判别式非负，根按照从小到大的顺序输出两个根；
# 如果判别式为0，输出两个相同的根；
# 否则，显示“No root”。输出系数、判别式和根均保留2位小数
import math

class QE:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def getA(self):
        return self.a

    def getB(self):
        return self.b

    def getC(self):
        return self.c

    def getD(self):
        return self.b ** 2 - 4 * self.a * self.c

    def getRoot1(self):
        d = self.getD()
        if d < 0:
            raise ValueError
        return (-self.b + math.sqrt(d)) / (2 * self.a)

    def getRoot2(self):
        d = self.getD()
        if d < 0:
            raise ValueError
        return (-self.b - math.sqrt(d)) / (2 * self.a)

a, b, c = map(float, input().split())
qe = QE(a, b, c)

print(f"a={qe.getA():.2f} b={qe.getB():.2f} c={qe.getC():.2f}")
print(f"det={qe.getD():.2f}")

try:
    r1 = qe.getRoot1()
    r2 = qe.getRoot2()
    if r1 > r2:
        r1, r2 = r2, r1
    print(f"root1={r1:.2f} root2={r2:.2f}")
except ValueError:
    print("No root")