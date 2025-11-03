# 题目描述
# 输入一个字符串，将该字符串中的大写英文字母按以下对应规则替换，输出替换后的字符串。
# 原字母    ： A B C D … X Y Z
# 对应字母 ： Z Y X W … C B A
s = input()

# 创建映射字典
mapping = {chr(65+i): chr(90-i) for i in range(26)}

# 使用列表推导式进行替换
result = ''.join(mapping.get(c, c) for c in s)

print(result)