# 题目描述
# 求列表或元组中整数元素求和，列表或元组中嵌套层次不限。
# 其中将部分相对独立功能使用函数完成。
# 提示函数isinstance(x, int)可以判断x是否为int类型数据。
def is_integer_element(element):
    """判断元素是否为整数"""
    return isinstance(element, int)

def sum_integers(data):
    """计算嵌套列表或元组中所有整数元素的和"""
    total = 0
    for item in data:
        if is_integer_element(item):
            # 如果是整数，直接累加
            total += item
        elif isinstance(item, (list, tuple)):
            # 如果是列表或元组，递归调用
            total += sum_integers(item)
    return total

# 读取输入并转换为Python对象
# 注意：这里假设输入是有效的Python列表或元组表达式
data = eval(input())

# 计算整数元素的和
result = sum_integers(data)

# 输出结果
print(result)