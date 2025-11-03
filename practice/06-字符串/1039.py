# 题目描述
# 英文辅音字母是除A、E、I、O、U以外的字母。
# 编写程序，统计给定字符串中大写辅音字母的个数。
s = input()
vowels = set("AEIOU")

count = 0
for char in s:
    if char.isupper() and char not in vowels:
        count += 1

print(count)