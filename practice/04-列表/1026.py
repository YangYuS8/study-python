# 题目描述
# 输入两个正整数m和n（m≤n），计算下面序列之和
# m*m + 1/m + (m+1)*(m+1) + 1/(m+1) + ⋯+ n*n + 1/n。
# 输出格式：保留5位小数。
m,n = map(int, input().split())
s = sum([i*i + 1/i for i in range(m,n+1)])
print(f"sum = {s:.5f}")