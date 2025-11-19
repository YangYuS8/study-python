# 题目描述
# 输入n对整数，计算这n对整数最大公约数之和。其中计算一对整数的最大公约数用函数实现。第一个整数为数对个数n，后续为n对整数。
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

n = int(input())

sum_gcd = 0

for i in range(1, n + 1):
    a, b = map(int, input().split())
    sum_gcd += gcd(a, b)

print(sum_gcd)