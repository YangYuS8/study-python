# 题目描述
# 输入n个整数，用空格分开。找出这n个数中的最大值及其对应的最小下标（下标从0开始）。
num = list(map(int, input().split()))
max_num = max(num)
min_site = num.index(max_num)
print(f'{max_num} {min_site}')