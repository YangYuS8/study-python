# 题目描述
# 一行中输入2个正整数a,b（1<=a<b），求[a,b)区间内分别能被3,5和7整除的数的个数，
# 以及同时能被3、5和7整除的数的个数，用集合实现。
a, b = map(int, input().split())
numbers = set(range(a, b))

# 使用集合推导式和集合运算
divisible_by_3 = {x for x in numbers if x % 3 == 0}
divisible_by_5 = {x for x in numbers if x % 5 == 0}
divisible_by_7 = {x for x in numbers if x % 7 == 0}
divisible_by_all = divisible_by_3 & divisible_by_5 & divisible_by_7

# 直接输出结果
print(len(divisible_by_3), len(divisible_by_5), len(divisible_by_7), len(divisible_by_all))