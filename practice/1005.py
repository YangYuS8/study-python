# 题目描述
# 输入三条边长a、b、c，如果能构成三角形，则计算并输出三角形的面积和周长，数值保留2位小数，
# 否则输出”These sides do not correspond to a valid triangle.”
import math

a,b,c = map(float,input().split())

if a+b<c or a+c<b or b+c<a:
    print("These sides do not correspond to a valid triangle.")
else:
    y = (a+b+c)/2
    x = y*(y-a)*(y-b)*(y-c)
    s = format(math.sqrt(x), '.2f')
    print("area = "+s+"; perimeter = "+format(y*2, '.2f'))