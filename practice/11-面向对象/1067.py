# 题目描述
# 设计一个银行个人账户类BankAccount。构造函数初始化账户余额；
# 提供取钱、存钱和查余额方法，余额不足不能支取；
# 同时提供月底时给账户增加利息功能，利息按月末余额计算，利率每个月都可能变化，利率作为参数传给计算利息方法。
# 测试程序如下：
"""
if __name__ == "__main__":
    balance = float(input())      #余额
    account = BankAccount(balance)
    money = float(input())        # 存钱金额
    account.deposit(money)
    money = float(input())        # 取钱金额
    account.withdraw(money)
    rate = float(input())         # 利率
    account.addInterest(rate)
    print(f"{account.getBalance():.2f}")
"""
class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount

    def getBalance(self):
        return self.balance

    def addInterest(self, rate):
        # 利率应为百分比，需要除以100
        interest = self.balance * (rate / 100)
        self.balance += interest

if __name__ == "__main__":
    balance = float(input())
    account = BankAccount(balance)
    money = float(input())
    account.deposit(money)
    money = float(input())
    account.withdraw(money)
    rate = float(input())
    account.addInterest(rate)
    print(f"{account.getBalance():.2f}")