# 题目描述
# 输入正整数N，计算序列 2/1 + 3/2 + 5/3 + 8/5 + ... 的前N项之和。
# 注意该序列从第2项起，每一项的分子是前一项分子与分母的和，分母是前一项的分子。
# 如果输入非正整数则输出"Invalid."，否则输出时保留3位小数。
try:
    N = int(input())
    if N <= 0:
        print("Invalid.")
    else:
        son = 2
        mom = 1
        sum = 0

        for i in range(N):
            sum += son / mom
            son, mom = son + mom, son

        print("{:.3f}".format(sum))
except:
    print("Invalid.")