# 题目描述
# 编写函数prime(n)判断n是否为素数，n为素数时返回True，否则返回False。
# 输入正整数m和n，输出区间[m, n]内所有素数的和。
import math

def prime(n):
    """使用math.sqrt的素数判断函数"""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    # 检查从3到√n的奇数
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

# 主程序
m, n = map(int, input().split())
total = sum(num for num in range(m, n + 1) if prime(num))
print(total)