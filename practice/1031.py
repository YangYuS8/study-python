# 题目描述
# 第一行输入正整数n（1<n≤10），随后输入一个n×n的方阵。
# 计算并输出该矩阵除副对角线、最后一列和最后一行以外的所有元素之和，保留2位小数。
# 副对角线为从矩阵的右上角至左下角的连线。
"""
# 读取矩阵大小
n = int(input())

# 读取矩阵
matrix = []
# _ 是一个变量名，表示我们不关心循环变量的值，只关心循环次数
for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

# 计算满足条件的元素之和
total = 0
for i in range(n):
    for j in range(n):
        # 排除副对角线、最后一行和最后一列
        if i != n-1 and j != n-1 and i + j != n-1:
            total += matrix[i][j]

# 输出结果，保留两位小数
print(f"{total:.2f}")
"""
n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
# TODO:为什么下划线可以作为变量使用？与正常变量的区别在哪里？

total = sum(matrix[i][j] for i in range(n-1) for j in range(n-1) if i + j != n-1)

print(f"{total:.2f}")