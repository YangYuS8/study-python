# 题目描述
# 输入一个非负整数n，生成一张3的乘方表，输出3 的0次幂 ~3的n次幂的值。
import math
n = int(input())

for i in range(0,n+1):
    print("pow(3,"+str(i)+") = "+str(int(math.pow(3,i))))