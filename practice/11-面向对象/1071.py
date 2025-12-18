# 题目描述
# 每天结束营业结束后，店长想知道一天的销售金额（结账金额）和客流量（结账人数）。
# 在收银机和收银机undo基础上，增加方法getSalesTotal和getSalesCount以获取当天的销售总金额和客流量。
# 提供一个日结resetSales方法返回当天的销售金额和客流量，并重置销售金额和客流量以便第二天的销售额从零开始。
# 测试程序如下：
"""
def readGood():             #输入购买商品的ID、单价和数量
    id, price, count = input().split()
    price = float(price)
    count = int(count)
    return id, price, count
if __name__ == "__main__":
    CashRegister.resetSales()                 # 前一天销售
    reg1 = CashRegister()
    id, price, count = readGood()
    reg1.addItem(id, price, count)
    total, count = reg1.checkOut()
    print(f"Total={total:.2f} Count={count}")
    salesTotal = CashRegister.getSalesTotal()
    salesCount = CashRegister.getSalesCount()
    print(f"SalesTotal={salesTotal:.2f} SalesCount={salesCount}")
    reg2 = CashRegister()
    id, price, count = readGood()
    reg2.addItem(id, price, count)
    total, count = reg2.checkOut()
    print(f"Total={total:.2f} Count={count}")
    salesTotal, salesCount = CashRegister.resetSales()    # 当天日结，下一天开始
    print(f"SalesTotal={salesTotal:.2f} SalesCount={salesCount}")
    CashRegister.resetSales()
    reg3 = CashRegister()
    id, price, count = readGood()
    reg3.addItem(id, price, count)
    total, count = reg3.checkOut()
    print(f"Total={total:.2f} Count={count}")
    salesTotal, salesCount = CashRegister.resetSales()    # 第二天日结
    print(f"SalesTotal={salesTotal:.2f} SalesCount={salesCount}")
"""
import copy

class CashRegister:
    # 类变量，记录所有收银机的销售总金额和客流量
    _sales_total = 0.0
    _sales_count = 0

    def __init__(self):
        self.items = {}  # 用字典存储商品，键为ID，值为(单价, 数量)
        self.total = 0.0  # 总金额
        self.count = 0  # 商品总数量
        self.history = []  # 保存历史状态，用于撤销

    def addItem(self, id, price, count):
        # 保存当前状态到历史
        self._save_state()

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

    def _save_state(self):
        """保存当前状态到历史"""
        state = {
            'items': copy.deepcopy(self.items),
            'total': self.total,
            'count': self.count
        }
        self.history.append(state)

    def undo(self):
        """撤销最后一次添加的商品"""
        if self.history:
            state = self.history.pop()
            self.items = state['items']
            self.total = state['total']
            self.count = state['count']

    def getTotal(self):
        return self.total

    def getCount(self):
        return self.count

    def checkOut(self):
        total = self.total
        count = self.count
        # 更新类变量：销售总金额和客流量
        CashRegister._sales_total += total
        CashRegister._sales_count += 1  # 每次结账代表一位顾客
        # 清空收银机
        self.items.clear()
        self.total = 0.0
        self.count = 0
        self.history.clear()  # 同时清空历史
        return total, count

    @classmethod
    def getSalesTotal(cls):
        return cls._sales_total

    @classmethod
    def getSalesCount(cls):
        return cls._sales_count

    @classmethod
    def resetSales(cls):
        total = cls._sales_total
        count = cls._sales_count
        cls._sales_total = 0.0
        cls._sales_count = 0
        return total, count

def readGood():  # 输入购买商品的ID、单价和数量
    id, price, count = input().split()
    price = float(price)
    count = int(count)
    return id, price, count

if __name__ == "__main__":
    CashRegister.resetSales()  # 前一天销售
    reg1 = CashRegister()
    id, price, count = readGood()
    reg1.addItem(id, price, count)
    total, count = reg1.checkOut()
    print(f"Total={total:.2f} Count={count}")
    salesTotal = CashRegister.getSalesTotal()
    salesCount = CashRegister.getSalesCount()
    print(f"SalesTotal={salesTotal:.2f} SalesCount={salesCount}")
    reg2 = CashRegister()
    id, price, count = readGood()
    reg2.addItem(id, price, count)
    total, count = reg2.checkOut()
    print(f"Total={total:.2f} Count={count}")
    salesTotal, salesCount = CashRegister.resetSales()  # 当天日结，下一天开始
    print(f"SalesTotal={salesTotal:.2f} SalesCount={salesCount}")
    CashRegister.resetSales()
    reg3 = CashRegister()
    id, price, count = readGood()
    reg3.addItem(id, price, count)
    total, count = reg3.checkOut()
    print(f"Total={total:.2f} Count={count}")
    salesTotal, salesCount = CashRegister.resetSales()  # 第二天日结
    print(f"SalesTotal={salesTotal:.2f} SalesCount={salesCount}")