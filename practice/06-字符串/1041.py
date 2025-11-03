# 题目描述
# 首先输入整数N，然后输入N个字符串，每个字符串占一行。
# 输出其中最长的字符串。
# 如果存在多个字符串具有相同的长度，则输出所有具有相同长度字符串。
N = int(input())
strings = [input().strip() for _ in range(N)]

max_length = max(len(s) for s in strings)

# 使用列表推导式筛选并输出
longest_strings = [s for s in strings if len(s) == max_length]
for s in longest_strings:
    print(s)