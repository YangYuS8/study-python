# 设计一个类Car模拟汽车。构造函数初始化汽车的燃油效率（单位为公里/升），同时油箱燃油初始化为0升；
# 提供一个drive方法，模拟在一定距离内驾驶汽车并减少燃油，提供方法getGas返回油箱剩余燃油，提供方法addGas添加燃油。
# 测试程序如下：
"""
if __name__ == "__main__":
    rate = int(input())     # 燃油效率
    myCar = Car(rate)
    gas = int(input())      # 添加燃油量
    myCar.addGas(gas)
    dis = float(input())    # 驾驶距离
    myCar.drive(dis)
    print(if __name__ == "__main__":
    rate = int(input())     # 燃油效率
    myCar = Car(rate)
    gas = int(input())      # 添加燃油量
    myCar.addGas(gas)
    dis = float(input())    # 驾驶距离
    myCar.drive(dis)
    print(f"{myCar.getGas():.2f}"))
"""
class Car:
    def __init__(self, rate):
        """初始化汽车，rate为燃油效率（公里/升），油箱初始为0"""
        self.rate = rate
        self.gas = 0.0  # 油箱燃油，单位升，用浮点数

    def addGas(self, gas):
        """添加燃油，gas为添加的量（单位升）"""
        self.gas += gas

    def drive(self, distance):
        """驾驶汽车一定距离（单位公里），消耗燃油"""
        # 计算所需燃油
        needed_gas = distance / self.rate
        # 如果燃油足够，则消耗
        if needed_gas <= self.gas:
            self.gas -= needed_gas
        else:
            # 如果燃油不足，则只能行驶到燃油用完
            # 实际行驶距离 = self.gas * self.rate
            # 但题目要求是模拟驾驶，这里我们选择消耗所有燃油
            # 如果题目要求不能驾驶，则可以选择不消耗燃油，但根据常理，燃油不足时会消耗所有燃油
            # 根据样例，我们假设燃油总是足够的，但为了健壮性，这里处理不足的情况
            # 这里我们选择消耗所有燃油，并打印一条信息（但题目没有要求输出，所以可以不打印）
            # 由于测试样例中燃油是足够的，我们可以先按足够处理，但为了代码完整性，这里处理不足
            self.gas = 0.0

    def getGas(self):
        """返回油箱剩余燃油（单位升）"""
        return self.gas

if __name__ == "__main__":
    rate = int(input())  # 燃油效率
    myCar = Car(rate)
    gas = int(input())  # 添加燃油量
    myCar.addGas(gas)
    dis = float(input())  # 驾驶距离
    myCar.drive(dis)
    print(f"{myCar.getGas():.2f}")