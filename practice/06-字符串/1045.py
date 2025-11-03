# 题目描述
# 输入一个字符串，提取字符串中的所有数字字符（'0'……'9'），
# 将相邻数字字符序列转换为一个整数，输出这些整数之和。
import re

s = input()

# 使用正则表达式找到所有连续的数字序列
numbers = re.findall(r'\d+', s)

# 将数字字符串转换为整数并求和
total = sum(map(int, numbers))

print(total)