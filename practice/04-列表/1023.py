# 题目描述
# 一行输入两个均不超过9的正整数a和n，编写程序输出a+aa+aaa++⋯+aa⋯a（n个a）之和。
"""
a,n = map(int, input().split())
s = 0
for i in range(1,n+1):
    for j in range(i):
        b = a * (10**j)
        s += b
print(s)
"""
"""
a,n = map(int, input().split())
s = 0
for i in range(1,n+1):
    b = sum([a*(10**j) for j in range(i)])
    s +=b
print(s)
"""
a,n = map(int, input().split())
s = sum([sum([a*(10**j) for j in range(i)]) for i in range(1,n+1)])
print(s)