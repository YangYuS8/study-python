# 题目描述
# 输入一个整数和这个整数的进制数，输出对应的十进制数。
a, b = input().split(', ')
c = int(a, int(b))
print(c)