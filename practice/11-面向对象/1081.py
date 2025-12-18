# 题目描述
# 以str为基类定义一个派生类RotatableStr，该类支持左右循环移位。
# 测试程序如下：
"""
if __name__ == "__main__":
    x = input()
    rstr = RotatableStr(x)
    print(rstr)
    rnum = int(input())
    rstr = rstr.rot_right(rnum)
    print(rstr)
    lnum = int(input())
    rstr = rstr.rot_left(lnum)
    print(rstr)
"""
class RotatableStr(str):
    def __new__(cls, value):
        # 使用 __new__ 方法创建字符串对象
        return super().__new__(cls, value)

    def rot_right(self, n):
        """返回右移 n 位后的新 RotatableStr 对象"""
        if len(self) == 0:
            return RotatableStr("")
        n = n % len(self)
        if n == 0:
            return RotatableStr(self)
        return RotatableStr(self[-n:] + self[:-n])

    def rot_left(self, n):
        """返回左移 n 位后的新 RotatableStr 对象"""
        if len(self) == 0:
            return RotatableStr("")
        n = n % len(self)
        if n == 0:
            return RotatableStr(self)
        return RotatableStr(self[n:] + self[:n])

if __name__ == "__main__":
    x = input()
    rstr = RotatableStr(x)
    print(rstr)
    rnum = int(input())
    rstr = rstr.rot_right(rnum)
    print(rstr)
    lnum = int(input())
    rstr = rstr.rot_left(lnum)
    print(rstr)