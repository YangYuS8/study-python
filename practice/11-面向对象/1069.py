# 题目描述
# 设计一个模拟收银机类CashRegister。一个收银机对象模拟顾客的一次购买结账。
# addItem方法可以将购买的某种商品条码、单价、数量记入收银机中；
# getTotal和getCount方法可以返回所有商品的应收金额以及商品数量；
# checkOut方法返回应收金额及商品数量，并清空所有数据成员。
# 测试程序如下：
"""
def readGood():             #输入购买商品的ID、单价和数量
    id, price, count = input().split()
    price = float(price)
    count = int(count)
    return id, price, count
if __name__ == "__main__":
    reg = CashRegister()
    id, price, count = readGood()
    reg.addItem(id, price, count)
    id, price, count = readGood()
    reg.addItem(id, price, count)
    print(f"Total={reg.getTotal():.2f} Count={reg.getCount()}")
    total, count = reg.checkOut()
    print(f"Total={total:.2f} Count={count}")

    id, price, count = readGood()
    reg.addItem(id, price, count)
    total, count = reg.checkOut()
    print(f"Total={total:.2f} Count={count}")
"""
class CashRegister:
    def __init__(self):
        self.items = {}  # 用字典存储商品，键为ID，值为(单价, 数量)
        self.total = 0.0  # 总金额
        self.count = 0  # 商品总数量

    def addItem(self, id, price, count):
        # 如果商品已存在，更新数量和总价
        if id in self.items:
            old_price, old_count = self.items[id]
            new_count = old_count + count
            self.total -= old_price * old_count  # 减去旧的总价
            self.total += price * new_count  # 加上新的总价
            self.items[id] = (price, new_count)
            self.count += count  # 只增加新增的数量
        else:
            self.items[id] = (price, count)
            self.total += price * count
            self.count += count

    def getTotal(self):
        return self.total

    def getCount(self):
        return self.count

    def checkOut(self):
        total = self.total
        count = self.count
        # 清空收银机
        self.items.clear()
        self.total = 0.0
        self.count = 0
        return total, count

def readGood():  # 输入购买商品的ID、单价和数量
    id, price, count = input().split()
    price = float(price)
    count = int(count)
    return id, price, count

if __name__ == "__main__":
    reg = CashRegister()
    id, price, count = readGood()
    reg.addItem(id, price, count)
    id, price, count = readGood()
    reg.addItem(id, price, count)
    print(f"Total={reg.getTotal():.2f} Count={reg.getCount()}")
    total, count = reg.checkOut()
    print(f"Total={total:.2f} Count={count}")

    id, price, count = readGood()
    reg.addItem(id, price, count)
    total, count = reg.checkOut()
    print(f"Total={total:.2f} Count={count}")