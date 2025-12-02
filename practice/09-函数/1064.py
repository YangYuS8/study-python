# 题目描述
# 第一行输入一个嵌套列表或元组，第二行输入层数，求该层的元素个数。
# 其中将部分相对独立功能使用函数完成。
# 提示函数isinstance(x, int)可以判断x是否为int类型数据。
def count_elements_at_level(data, target_level, current_level=1):
    """统计嵌套结构中指定层数的元素个数"""
    if current_level == target_level:
        # 如果当前层就是目标层，直接返回当前层的元素个数
        return len(data)

    count = 0
    for item in data:
        if isinstance(item, (list, tuple)):
            # 如果是嵌套结构，递归进入下一层
            count += count_elements_at_level(item, target_level, current_level + 1)
    return count


# 读取嵌套结构
data = eval(input())

# 读取目标层数
level = int(input())

# 计算指定层数的元素个数
result = count_elements_at_level(data, level)

# 输出结果
print(result)