# 题目描述
# 编写函数fib(n)返回第n项Fibonacci数，其中fib(0)=fib(1)=1。
# 输入m和n（1<m<n），输出[m,n]内Fibonacci数的个数。
def fib(n):
    """返回第n项Fibonacci数"""
    if n == 0 or n == 1:
        return 1

    a, b = 1, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


# 主程序
m, n = map(int, input().split())

count = 0
i = 0
while True:
    current_fib = fib(i)
    if current_fib > n:
        break
    if current_fib >= m:
        count += 1
    i += 1

print(count)