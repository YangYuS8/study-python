import math
line1 = float(input())
line2 = float(input())
line3 = float(input())
s = (line1+line2+line3)/2
area = math.sqrt(s*(s-line1)*(s-line2)*(s-line3))
print(f"area: {area}")