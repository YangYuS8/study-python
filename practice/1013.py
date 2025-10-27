# 题目描述
# 输入一组学生成绩，计算学生的平均成绩，并统计及格（成绩不低于60分）的人数。
# 输入格式：第一行为学生人数N，第二行为N个学生成绩
# 输出格式：平均成绩保留1位小数。
n = int(input())
scores = list(map(int, input().split()))

# 使用列表推导式和内置函数
count = len([scores for scores in scores if scores >= 60])
avg = sum(scores) / n

print(f"average = {avg:.1f}")
print(f"count = {count}")