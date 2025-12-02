
# 编写程序读取文本文件freedom. txt，统计每一个单词出现的次数，
# 单词不区分大小写，按照单词的字典顺序输出到“dic. txt”文件保存，
# 输出格式为每行一个单词及其出现的次数。
import re
from collections import Counter

with open('practice/10-文件/freedom.txt', encoding='utf-8') as f:
  text = f.read().lower()

words = re.findall(r"[a-z']+", text)
counts = Counter(words)

with open('practice/10-文件/dic.txt', 'w', encoding='utf-8') as f:
  for word in sorted(counts):
    f.write(f"{word} {counts[word]}\n")