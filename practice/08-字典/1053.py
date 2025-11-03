# 题目描述
# 给输入公司N名员工的工龄，按工龄增序输出每个工龄的员工数量。
# 直接读取一行工龄数据
ages = list(map(int, input().split()))

# 使用字典统计每个工龄的员工数量
age_count = {}
for age in ages:
    age_count[age] = age_count.get(age, 0) + 1

# 按工龄递增顺序输出，使用冒号分隔
for age in sorted(age_count.keys()):
    print(f"{age}:{age_count[age]}")