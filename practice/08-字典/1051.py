# 题目描述
# 使用字典存储星期一到星期日的名称Mon、Tue、Wed、Thu、Fri、Sat、Sun。
# 输入一个1到7的数字，输出对应的星期名的缩写。
# 创建数字到星期名缩写的字典
week_dict = {
    1: "Mon",
    2: "Tue",
    3: "Wed",
    4: "Thu",
    5: "Fri",
    6: "Sat",
    7: "Sun"
}

# 读取输入的数字
day_number = int(input())

# 输出对应的星期名缩写
print(week_dict[day_number])