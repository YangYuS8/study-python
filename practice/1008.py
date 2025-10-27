# 题目描述
# 编写一个程序，读取4个整数。
# 如果输入的是两组相等的数值对（顺序可以相同也可以不同），则打印“two pairs”；
# 否则，打印“not two pairs”。
# 例如：2 1 2 1、2 1 1 2、2 2 1 1、2 2 2 2等都是two pairs，1 2 2 3则是 not two pairs
a,b,c,d=map(int,input().split())
if a==b and c==d or a==c and b==d or a==d and b==c:
    print("two pairs")
else:
    print("not two pairs")