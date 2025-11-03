# 题目描述
# 输入一个正整数m，如果m>=11则计算并输出 11+12+13+...+m 的值，否则输出0。
"""
m = int(input())
sum = 0
if m >= 11:
    for i in range(11, m + 1):
        sum += i
    print(sum)
else:
    print(0)
"""

m = int(input())
s = sum([i for i in range(11,m+1)])
print(s)