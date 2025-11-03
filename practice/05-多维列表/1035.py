# 题目描述
# 第一行输入一个正整数M，接下来输入M个方阵的信息：
# 每个方阵信息的第一行为不超过10的正整数n，随后是n×n方阵。
# 判断每个方阵是否上三角矩阵，如果是输出“YES”，否则输出“NO”。
# 上三角矩阵指主对角线以下的元素都为0的矩阵，每个矩阵的判断结果占一行。
M = int(input())
for _ in range(M):
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]

    # 使用any和生成器表达式判断
    # TODO:
    is_upper_triangular = not any(
        matrix[i][j] != 0
        for i in range(n)
        for j in range(i)
    )

    print("YES" if is_upper_triangular else "NO")