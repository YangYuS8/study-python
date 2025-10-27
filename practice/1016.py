# 题目描述
# 判断一个给定的正整数是否素数。
#
# 输入格式:第一行为一个正整数N（≤ 10），随后N行，每行一个正整数
# 输出格式:N行判断结果。如果它是素数，则在一行中输出Yes，否则输出No
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

n = int(input())
for i in range(n):
    x = int(input())
    if is_prime(x):
        print("Yes")
    else:
        print("No")