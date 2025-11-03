# 题目描述
# 输入两个整数A和B（A,B<10000），顺序输出从A到B的所有整数，
# 每行5个整数，每个整数占5个字符宽度，右对齐。最后按Sum = X的格式输出这些整数和X。
A,B = map(int,input().split())

total = 0
count = 0

for num in range(A,B+1):
    print(f"{num:>5}", end="")
    total += num
    count += 1

    if count % 5 == 0:
        print()

if count % 5 != 0:
    print()

print(f"Sum = {total}")