# 题目描述
# 输入一个十进制正整数，将其转换为十六进制数。
# 如整数1123021的十六进制数为0x1122cd，再输入一个字符（1,2,3,4,5,6,7,8,9,a,b,c,d,e,f），
# 统计这个字符在这个十六进制数中出现的次数。如输入1，1在0x1122cd中出现2次，则输出2。
# 读取十进制正整数
decimal_num = int(input())

# 读取要统计的字符
target_char = input().strip().lower()

# 将十进制数转换为十六进制字符串（不带0x前缀）
hex_str = hex(decimal_num)[2:]

# 统计字符在十六进制字符串中出现的次数
count = hex_str.count(target_char)

# 输出结果
print(count)