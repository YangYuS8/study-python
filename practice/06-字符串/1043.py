# 题目描述
# 输入一个单词，打印单词中的音节数。
# 假设音节按如下方式确定：每个相邻的元音序列a e i o u y（除了单词中的最后一个e外），
# 都是一个音节。但是如果该算法产生的计数为0，则将其更改为1。
# 如：单词your、chocolate、network、the的音节数分别为1、3、2、1。
word = input().strip().lower()
vowels = set('aeiouy')

# 处理末尾的'e'
processed_word = word[:-1] if word.endswith('e') else word

# 统计元音序列
count = 0
prev_consonant = True  # 标记前一个字符是否为辅音

for char in processed_word:
    if char in vowels:
        if prev_consonant:
            count += 1
            prev_consonant = False
    else:
        prev_consonant = True

# 处理结果为0的情况
print(max(1, count))