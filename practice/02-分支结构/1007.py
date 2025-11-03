# 题目描述
# 编写一个程序，读入3个数值。如果它们按递增顺序排列，则打印ASC；
# 如果它们按递减顺序排列，则打印DES；
# 否则，打印No Order。假设序列3 4 4不是按递增顺序排列的。
a,b,c=map(float,input().split())
if a<b<c:
    print("ASC")
elif a>b>c:
    print("DES")
else:
    print("No Order")