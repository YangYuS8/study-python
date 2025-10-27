# 题目描述
# 输入一个正整数N，计算序列 1 + 1/3 + 1/5 + ... 的前N项之和并输出。
# 输出格式为：“sum = S”，保留5位小数。
n = int(input())
s = sum([1/(2*i+1) for i in range(n)])
print("sum =",'%.5f' % s)