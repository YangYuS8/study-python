# 题目描述
# 给定四种水果，分别是苹果（apple）、梨（pear）、桔子（orange）、葡萄（grape），
# 单价分别对应为3.00元/公斤、2.50元/公斤、4.10元/公斤、10.20元/公斤。
# 首先在屏幕上显示以下菜单：
# [1] apple
# [2] pear
# [3] orange
# [4] grape
# [0] exit
# 用户输入一行编号（1~4），显示编号对应水果的单价。
# 如果编号个数达到5次时，程序应自动退出查询；
# 不到5次而用户输入0也退出；
# 输入其他编号，显示价格为0。单价显示保留2位小数。
# 显示菜单
print("[1] apple")
print("[2] pear")
print("[3] orange")
print("[4] grape")
print("[0] exit")

# 读取一行输入并按空格分割
inputs = input().split()

# 只处理前4个输入，无论是否有更多
for i in range(min(4, len(inputs))):
    num_str = inputs[i]

    try:
        choice = int(num_str)

        # 如果输入0，退出循环
        if choice == 0:
            break

        # 根据选择显示价格
        if choice == 1:
            print("price = 3.00")
        elif choice == 2:
            print("price = 2.50")
        elif choice == 3:
            print("price = 4.10")
        elif choice == 4:
            print("price = 10.20")
        else:
            # 其他编号显示0.00
            print("price = 0.00")

    except ValueError:
        # 如果转换失败（非整数），价格为0.00
        print("price = 0.00")