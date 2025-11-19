# 题目描述
# 一行输入多个单词，输出所有单词的音节数之和。计算一个单词的音节数用函数实现。
# 假设音节按如下方式确定：每个相邻的元音序列a e i o u y（除了单词中的最后一个e外），都是一个音节。
# 但是如果该算法产生的计数为0，则将其更改为1。如：单词your、chocolate、network、the的音节数分别为1、3、2、1。
def count_syllables(word):
    vowels = set('aeiouy')

    if not word:
        return 1

    word = word.lower()

    if word.endswith('e'):
        processed_word = word[:-1]
    else:
        processed_word = word

    syllable_count = 0
    prev_consonant = True

    for char in processed_word:
        if char in vowels:
            if prev_consonant:
                syllable_count += 1
                prev_consonant = False
        else:
            prev_consonant = True

    return max(1, syllable_count)


# 读取输入并计算总音节数
words = input().split()
total_syllables = sum(count_syllables(word) for word in words)

print(total_syllables)