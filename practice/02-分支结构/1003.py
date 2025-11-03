import math
x=float(input())
if x == 0:
    y = format(x, '.2f')
else:
    y = format(1/x, '.2f')
print("f("+format(x, '.2f')+") =", y)