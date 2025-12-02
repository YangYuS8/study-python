# 读取一个包含两列浮点数的文件data.txt，打印每列的平均值，保留2位小数。
sums = [0.0, 0.0]
count = 0
with open('practice/10-文件/data.txt', 'r', encoding='utf-8') as f:
  for line in f:
    line = line.strip()
    if not line:
      continue
    parts = line.split()
    if len(parts) < 2:
      continue
    try:
      a, b = float(parts[0]), float(parts[1])
    except ValueError:
      continue
    sums[0] += a
    sums[1] += b
    count += 1

if count == 0:
  print("No valid data.")
else:
  print(f"{sums[0]/count:.2f}")
  print(f"{sums[1]/count:.2f}")