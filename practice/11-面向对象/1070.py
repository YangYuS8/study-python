# 题目描述
# 在收银机类CashRegister基础上，增加一个undo方法允许撤销最后一次添加的商品。
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
    id, price, count = readGood()
    reg.addItem(id, price, count)
    print(f"Total={reg.getTotal():.2f} Count={reg.getCount()}")
    reg.undo()
    reg.undo()
    total, count = reg.checkOut()
    print(f"Total={total:.2f} Count={count}")
"""
import copy

class CashRegister:
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
        # 清空收银机
        self.items.clear()
        self.total = 0.0
        self.count = 0
        self.history.clear()  # 同时清空历史
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
    id, price, count = readGood()
    reg.addItem(id, price, count)
    print(f"Total={reg.getTotal():.2f} Count={reg.getCount()}")
    reg.undo()
    reg.undo()
    total, count = reg.checkOut()
    print(f"Total={total:.2f} Count={count}")