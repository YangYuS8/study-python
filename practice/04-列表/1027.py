# 题目描述
# 一行输入若干名学生的身高，其中以空格分隔，每个身高都是一个正整数。
# 计算他们的平均身高，输出超过平均身高的输入值，每个数后面有一个空格，输出的顺序和输入的相同。
heights = list(map(int, input().split()))
avg_height = sum(heights) / len(heights)
print(' '.join(str(h) for h in heights if h > avg_height), end=" ")