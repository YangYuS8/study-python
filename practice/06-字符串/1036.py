# 题目描述
# 一个合法的身份证号码由17位地区、日期编号和顺序编号加1位校验码组成。校验码的计算规则如下：
# 首先对前17位数字加权求和，权重分配为：{7，9，10，5，8，4，2，1，6，3，7，9，10，5，8，4，2}；
# 然后将计算的和对11取模得到值Z；最后按照以下关系对应Z值与校验码M的值：
# Z：0 1 2 3 4 5 6 7 8 9 10
# M：1 0 X 9 8 7 6 5 4 3 2
# 现在给定一些身份证号码，请你验证校验码的有效性，并输出有问题的号码。

# 输入格式：第一行为身份证号码的个数N。随后N行，每行给出1个18位身份证号码。
# 输出格式：按照输入的顺序每行输出1个有问题的身份证号码。
# 这里只检查前17位是否全为数字且最后1位校验码计算准确。如果所有号码都正常，则输出All passed。
N = int(input())
weights = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
M_map = '10X98765432'

invalid_ids = []
for _ in range(N):
    id_card = input().strip()

    # 检查前17位是否都是数字
    if not id_card[:17].isdigit():
        invalid_ids.append(id_card)
        continue

    # 计算加权和和校验码
    # TODO:什么是加权求和？我不理解
    total = sum(int(id_card[i]) * weights[i] for i in range(17))
    if id_card[17] != M_map[total % 11]:
        invalid_ids.append(id_card)

print('\n'.join(invalid_ids) if invalid_ids else "All passed")