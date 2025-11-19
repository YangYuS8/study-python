# 题目描述
# 编写函数fn(a,n) 求表达式a+aa+aaa+⋯+aa⋯aa(n个a）之和，其中a和n均为不超过9的正整数。
# 一行输入多对a和n，求这多对a和n构成的表达式之和。如输入2 3 4 2，应输出2+22+222+4+44的和294。
def fn(a, n):
    # 公式：a * (10^(n+1) - 9*n - 10) / 81
    return a * (10**(n+1) - 9*n - 10) // 81

# 读取输入
data = list(map(int, input().split()))

# 计算所有表达式之和
total_sum = 0
for i in range(0, len(data), 2):
    a = data[i]
    n = data[i+1]
    total_sum += fn(a, n)

print(total_sum)