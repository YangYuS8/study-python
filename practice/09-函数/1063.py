# 题目描述
# 输入一个嵌套列表或元组，嵌套层次不限，根据层次，求列表元素的个数加权和。
# 第1层元素权重为1，第2层元素的权重为2，第3层元素权重为3，...，以此类推！
# 其中将部分相对独立功能使用函数完成。
# 提示函数isinstance(x, int)可以判断x是否为int类型数据。
def calculate_count_weighted_sum(data, level=1):
    """计算嵌套列表或元组中元素个数的加权和"""
    total = 0
    for item in data:
        # 每个元素都按当前层次的权重计数
        total += level
        if isinstance(item, (list, tuple)):
            # 如果是列表或元组，递归调用，层次加1
            total += calculate_count_weighted_sum(item, level + 1)
    return total

# 读取输入并转换为Python对象
data = eval(input())

# 计算元素个数的加权和
result = calculate_count_weighted_sum(data)

# 输出结果
print(result)