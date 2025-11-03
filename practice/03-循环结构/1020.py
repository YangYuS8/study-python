# 题目描述
# 输入一个正整数n，输出1!+3!+5!+……+n!的和。
import math
n = int(input())
s = 0
for i in range(1, n+1, 2):
    s += math.factorial(i)
print(f"n = {n}, s = {s}")