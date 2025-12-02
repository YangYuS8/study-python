# 编写程序读取文本文件score.txt。
# 文件每行是一名学生的姓名、平时成绩和期末成绩，
# 读取文件按照平时和期末分别占总成绩的40%和60%计算总成绩（四舍五入取整），
# 按照score文件中学生顺序输出所有学生的姓名、平时成绩、期末成绩和总成绩。
# 输出时，先输出一行表头，再输出每个学生信息，
# 各项数据之间用逗号(,)分隔，每行最后不输出逗号。
import os

def fmt_score(x):
  if isinstance(x, float) and x.is_integer():
    return str(int(x))
  s = str(x)
  if '.' in s:
    s = s.rstrip('0').rstrip('.')
  return s

records = []
path = './practice/10-文件/score.txt'
if not os.path.isfile(path):
  raise FileNotFoundError(f"File not found: {path}")

with open(path, 'r', encoding='utf-8') as f:
  for line in f:
    line = line.strip()
    if not line:
      continue
    parts = [p.strip() for p in line.split(',') if p.strip()]
    if len(parts) < 3:
      parts = [p.strip() for p in line.split() if p.strip()]
    if len(parts) < 3:
      continue
    name = parts[0]
    try:
      usual = float(parts[1])
      final = float(parts[2])
    except ValueError:
      continue
    total = int(usual * 0.4 + final * 0.6 + 0.5)
    records.append((name, usual, final, total))

print('姓名,平时成绩,期末成绩,总成绩')
for name, usual, final, total in records:
  print(','.join([name, fmt_score(usual), fmt_score(final), str(total)]))