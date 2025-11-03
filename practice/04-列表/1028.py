# 题目描述
# 在一行中输入整数序列，整数之间以空格分隔。
# 统计整型序列中出现次数最多的整数及其出现次数。
# 题目保证这样的数字是唯一的。
from collections import Counter
num = list(map(int, input().split()))
count = Counter(num)
# counter.most_common(1) - 返回出现次数最多的 1 个元素
# 返回值是一个列表，包含元组，格式是 [(元素, 出现次数)]
# [0] - 取列表中的第一个元素，也就是 (元素, 出现次数)
# most_common_num, max_count = ... - 将元组解包，
# 把 2 赋值给 most_common_num，5 赋值给 max_count
most_common, max_count = count.most_common(1)[0]
print(f"{most_common} {max_count}")