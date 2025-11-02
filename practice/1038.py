# 题目描述
# 编写程序，输入一个字符和一个字符串，查找字符在字符串中是否存在。
# 如果存在则按照格式“index = 下标”输出该字符在字符串中所对应的最大下标（下标从0开始）；
# 否则输出"Not Found"。
str1 = str(input())
string = str(input())
index = 0
count = 0
for i in range(len(string)):
    if string[i] == str1 and i >= index:
        index = i
        count += 1
if count > 0:
    print(f"index = {index}")
else:
    print("Not Found")