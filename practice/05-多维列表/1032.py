# 题目描述
# 第一行输入两个正整数m和n（1≤m,n≤6）。随后输入m×n矩阵。
# 计算并输出该矩阵每行元素之和，保留2位小数。
m, n = map(int, input().split())
matrix = [list(map(float, input().split())) for _ in range(m)]

# 直接计算并输出每行的和
for row in matrix:
    print(f"{sum(row):.2f}")
# TODO:为什么不需要使用n也能正常运行？