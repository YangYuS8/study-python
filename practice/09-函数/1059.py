# 题目描述
# 一行输入多个单词，输出回文的个数。回文就是字符串中心对称，从左向右读和从右向左读的内容是一样的。判断一个单词是否为回文用函数实现。
def is_palindrome(word):
    return word == word[::-1]

# 读取输入并统计回文单词个数
words = input().split()
count = sum(1 for word in words if is_palindrome(word))

print(count)