# 题目描述
# 输入9个小于100的整数，其间各以一个空格间隔，将其组成一个3×3矩阵，并将此矩阵转置（即行和列互换）。
# 输出转置前和转置后的矩阵，输出的每个数据输出占4列。

# 读取输入并构建矩阵
numbers = list(map(int, input().split()))
matrix = [numbers[i:i+3] for i in range(0, 9, 3)]

# 输出原矩阵
print("before transposition")
for row in matrix:
    print(''.join(f"{num:4d}" for num in row))

# 构建并输出转置矩阵
print("after transposition")
transposed = list(zip(*matrix))
# TODO:zip的具体用法还需要去熟悉一下
for row in transposed:
    print(''.join(f"{num:4d}" for num in row))