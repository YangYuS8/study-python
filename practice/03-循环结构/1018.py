# 题目描述
# 输入一行字符，统计其中英文字母、空格、数字字符和其他字符的个数。
#
# 输入格式:最后一个回车表示输入结束，不算在内。
# 输出格式:
# letter = 英文字母个数, blank = 空格个数, digit = 数字字符个数, other = 其他字符个数
n = input()

letter = 0
blank = 0
digit = 0
other = 0

for i in n:
    if i.isalpha():
        letter += 1
    elif i.isdigit():
        digit += 1
    elif i == " ":
        blank += 1
    else:
        other += 1

print(f"letter = {letter}, blank = {blank}, digit = {digit}, other = {other}")
