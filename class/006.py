# 求两点（x1,y1）与(x2,y2)间距离
import math
x1, y1 = 3, 4
x2, y2 = 4, 4
# Compute the distance between the two points
distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print(f"Distance: {distance}")