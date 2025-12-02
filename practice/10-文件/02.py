# 编写一个程序读取文本文件“example. txt”，将其中的大写字母变为小写字母，
# 小写字母变为大写字母，其他字符不变，结果写入文件“result. txt”。
def swap_case_file(src='./practice/10-文件/example.txt', dst='./practice/10-文件/result.txt', encoding='utf-8'):
  try:
    with open(src, 'r', encoding=encoding) as f:
      content = f.read()
  except FileNotFoundError:
    print(f"源文件未找到: {src}")
    return
  except Exception as e:
    print("读取文件出错:", e)
    return

  swapped = content.swapcase()

  try:
    with open(dst, 'w', encoding=encoding) as f:
      f.write(swapped)
  except Exception as e:
    print("写入文件出错:", e)
    return

  print(f"已将结果写入: {dst}")

if __name__ == '__main__':
  swap_case_file()