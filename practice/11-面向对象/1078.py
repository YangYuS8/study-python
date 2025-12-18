# 题目描述
# 编写程序，一行输入若干个正整数，输出每个正整数的各个数位上的奇数数字乘积。其中计算一个正整数的各个数位上的奇数数字乘积用函数实现。
"""
# 第一个空

    mul = 1
    while x>0:
        digit = x % 10
        # 第二个空

            mul *= digit
        x //= 10
    return mul


if __name__ == "__main__":
    data = map(int, input().split())
    for item in data:
        result = calmul(item)
        # 第三个空
"""
def calmul(x):
    mul = 1
    while x > 0:
        digit = x % 10
        if digit % 2 == 1:
            mul *= digit
        x //= 10
    return mul

if __name__ == "__main__":
    data = map(int, input().split())
    results = []
    for item in data:
        results.append(str(calmul(item)))
    print(' '.join(results))