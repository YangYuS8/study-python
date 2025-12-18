# 题目描述
# 以list为基类定义一个派生类RotatableList，该类支持左右循环移位。
# 测试程序如下：
"""
if __name__ == "__main__":
    x = input().split()
    rlist = RotatableList(x)
    print(rlist)
    rnum = int(input())
    rlist.rot_right(rnum)
    print(rlist)
    lnum = int(input())
    rlist.rot_left(lnum)
    print(rlist)
"""
class RotatableList(list):
    def __init__(self, items):
        # 如果传入的是字符串，则按空格分割成列表
        if isinstance(items, str):
            items = items.split()
        super().__init__(items)

    def __str__(self):
        return " ".join(self)

    def rot_right(self, n):
        if len(self) == 0:
            return
        n = n % len(self)
        if n == 0:
            return
        self[:] = self[-n:] + self[:-n]

    def rot_left(self, n):
        if len(self) == 0:
            return
        n = n % len(self)
        if n == 0:
            return
        self[:] = self[n:] + self[:n]

if __name__ == "__main__":
    x = input().strip()
    rlist = RotatableList(x)
    print(rlist)
    rnum = int(input())
    rlist.rot_right(rnum)
    print(rlist)
    lnum = int(input())
    rlist.rot_left(lnum)
    print(rlist)