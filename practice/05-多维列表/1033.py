# 题目描述
# 给定M行N列的整数矩阵A，如果A的非边界元素A[i][j]大于相邻的上下左右4个元素，
# 那么就称元素A[i][j]是矩阵的局部极大值。
# 本题要求给定矩阵的全部局部极大值及其所在的位置。

# 输入格式：
# 输入在第一行中给出矩阵A的行数M和列数N（3≤M,N≤20）；
# 最后M行，每行给出A在该行的N个元素的值，元素值为整数。数值以空格分隔。

# 输出格式：
# 每行按照“元素值 行号 列号”的格式输出一个局部极大值，其中行、列编号从1开始。要求按照行号递增输出；
# 若同行有超过1个局部极大值，则该行按列号递增输出。
# 若没有局部极大值，则输出“None 总行数 总列数”。
M, N = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(M)]

# 一行代码查找所有局部极大值
results = [(matrix[i][j], i+1, j+1)
    for i in range(1, M-1) for j in range(1, N-1)
    if all(matrix[i][j] > matrix[i+dx][j+dy]
    for dx, dy in [(0,1), (0,-1), (1,0), (-1,0)])]
# TODO:这个推导式还需要研究一下，不太容易理解

# 输出结果
print('\n'.join(f"{v} {r} {c}" for v, r, c in results) if results else f"None {M} {N}")