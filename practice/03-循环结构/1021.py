# 题目描述
# 输入一个正整数N（N>1），将N分解为素数的乘积。
# from sympy import isprime
n = int(input())
factors = []
i = 2
# if isprime(n):
#     print(n)
# else:
while n > 1:
    if n % i == 0:
        factors.append(i)
        n = n / i
    else:
        i += 1
for i in factors:
    print(i, end=' ')