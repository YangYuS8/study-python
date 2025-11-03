# 题目描述
# 输入用字符串表示两个字典，字典的键为一个字符或一个数字。
# 将两个字典合并，如果两个字典中具有相同的键，合并时值做加法运算。
# 将合并后的字典按键升序输出。
# 注意：1和'1'是不同的键，输出是按字典序输出，'1' 的 ASCII 码为 49，大于 1，排序时 1 在前，'1'在后。
# 读取并转换字典
dict1 = eval(input().strip())
dict2 = eval(input().strip())

# 合并字典
merged = {}
for d in [dict1, dict2]:
    for k, v in d.items():
        merged[k] = merged.get(k, 0) + v

# 分离并排序键
num_keys = sorted([k for k in merged if isinstance(k, int)])
str_keys = sorted([k for k in merged if isinstance(k, str)])

# 构建输出
items = [f"'{k}': {merged[k]}" if isinstance(k, str) else f"{k}: {merged[k]}"
         for k in num_keys + str_keys]

print("{" + ", ".join(items) + "}")