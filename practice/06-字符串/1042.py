# 题目描述
# 首先输入整数N，然后输入N个字符串，每个字符串占一行。
# 输出回文的个数。
# 回文就是字符串中心对称，从左向右读和从右向左读的内容是一样的。
N = int(input())

# 使用列表推导式统计回文字符串
count = sum(1 for _ in range(N) if (s := input().strip()) == s[::-1])

print(count)