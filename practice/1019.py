# 题目描述
# 输入一笔零钱数额x∈(8,100)，将x换成5分、2分和1分的硬币，要求每种硬币至少有一枚，输出换法数量及每一种换法。
x = int(input())

count = 0

for fen5 in range((x-3)//5, 0, -1):
    for fen2 in range((x-5*fen5-1)//2, 0, -1):
        fen1 = x-5*fen5-2*fen2
        if fen1 >=1:
            count += 1
            print(f"fen5:{fen5}, fen2:{fen2}, fen1:{fen1}")

print(f"count =  {count}")