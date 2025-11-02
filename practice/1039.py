# 题目描述
# 英文辅音字母是除A、E、I、O、U以外的字母。
# 编写程序，统计给定字符串中大写辅音字母的个数。
string = str(input())
set1 = {'A', 'E', 'I', 'O', 'U'}
for i in range (len(string)):
    if string[i] in set1:
