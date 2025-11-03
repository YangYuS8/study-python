# 题目描述
# 输入两个正整数M和N（M<=N），输出[M, N]区间内素数的个数及这些素数的和。
def is_prime(num):
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num**0.5) + 1, 2):  # 只检查奇数
        if num % i == 0:
            return False
    return True


def main():
    M, N = map(int, input().split())
    count = 0
    total = 0
    # 遍历区间内的所有数
    for num in range(M, N + 1):
        if is_prime(num):
            count += 1
            total += num

    print(count, total)

if __name__ == "__main__":
    main()