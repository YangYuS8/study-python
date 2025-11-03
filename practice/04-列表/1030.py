# 题目描述
# 输入两组整数，每组数占一行，输出不是两者共有的元素。同一数字不重复输出。先输出第一组数，后输出第二组数。
num1 = list(map(int, input().split()))
num2 = list(map(int, input().split()))

# 使用集合操作找出独有元素
set1 = set(num1)
set2 = set(num2)

# 找出第一组中独有的元素（保持顺序）
unique1 = []
seen = set()
for num in num1:
    # 集合的差集操作: 返回在 set1 中但不在 set2 中的所有元素
    if num in set1 - set2 and num not in seen:
        unique1.append(num)
        seen.add(num)

# 找出第二组中独有的元素（保持顺序）
unique2 = []
seen = set()
for num in num2:
    if num in set2 - set1 and num not in seen:
        unique2.append(num)
        seen.add(num)

# 输出结果
print(' '.join(map(str, unique1 + unique2)))