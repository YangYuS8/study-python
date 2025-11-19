# 题目描述
# 编写函数def merge(a, b)以合并两个列表，返回的列表是交替排列两个列表的元素。
# 如果一个列表比另一个列表短，则先尽量交替排列，最后附加长列表中的剩余元素。
# 例如列表a为[1, 4, 9, 16]，列表b为[9, 7, 4, 9, 11, 45]，
# 则merge(a,b)返回一个新的列表，包含一下值：[1, 9, 4, 7, 9, 4, 16, 9, 11, 45]。
# 输入两个列表，调用merge函数合并这两个列表并输出。
def merge(a, b):
    """合并两个列表，交替排列元素"""
    result = []
    min_len = min(len(a), len(b))

    # 交替添加元素，直到较短列表用完
    for i in range(min_len):
        result.append(a[i])
        result.append(b[i])

    # 添加较长列表的剩余元素
    result.extend(a[min_len:])
    result.extend(b[min_len:])

    return result


# 主程序
a = eval(input())
b = eval(input())
print(merge(a, b))