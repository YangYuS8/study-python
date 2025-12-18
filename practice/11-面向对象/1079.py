# 题目描述
# 编写程序，输入一个正整数n，求它的所有因数之和。如6的因数为1、2、3、6，则因数之和为12。
n = int(input())
total = 0

for i in range(1, int(n ** 0.5) + 1):
    if n % i == 0:
        total += i
        if i != n // i:  # 避免重复计算平方根
            total += n // i

print(total)