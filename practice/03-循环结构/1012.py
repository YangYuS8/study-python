# 题目描述
# 输入正整数N，输出菲波那契（Fibonacci）数列的前N（1≤N≤46）项，每行输出5个，每个数占11位。
# Fibonacci数列就是满足任一项数字是前两项的和（最开始两项均定义为1）的数列，例如：1，1，2，3，5，8，13，...。
# 如果N小于1，则输出"Invalid."
N = int(input())

if N < 1:
    print("Invalid.")
else:
    a, b = 0, 1
    for i in range(N):
        # 使用a, b = b, a+b可以同时更新两个值
        a, b = b, a + b
        print(f"{a:11d}", end="")

        if (i + 1) % 5 == 0:
            print()

    if N % 5 != 0:
        print()