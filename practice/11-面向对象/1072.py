# 题目描述
# 设计一个菜单类Menu。Menu类对象可以添加一个菜单选项addOption方法，也包含一个获取用户输入的getInput方法。
# getInput方法首先显示所有菜单选项，然后接收用户的输入，如果用户输入无效则重新显示菜单并重新接收用户输入，
# 直至用户输入有效为止，最后返回用户的有效选择的菜单项序号（从1起）。
# 测试程序如下：
"""
if __name__ == "__main__":
    mainMenu = Menu()
    option = input()
    mainMenu.addOption(option)
    option = input()
    mainMenu.addOption(option)
    option = input()
    mainMenu.addOption(option)
    choice = mainMenu.getInput()
    print(choice)
"""
class Menu:
    def __init__(self):
        self.options = []

    def addOption(self, option):
        self.options.append(option)

    def getInput(self):
        while True:
            # 显示菜单选项（格式与样例一致）
            for i, option in enumerate(self.options, 1):
                print(f"{i} {option}")

            try:
                choice = int(input())
                if 1 <= choice <= len(self.options):
                    return choice
                # 如果不在有效范围，继续循环（不打印错误信息）
            except ValueError:
                # 输入非数字，继续循环（不打印错误信息）
                pass

if __name__ == "__main__":
    mainMenu = Menu()
    option = input()
    mainMenu.addOption(option)
    option = input()
    mainMenu.addOption(option)
    option = input()
    mainMenu.addOption(option)
    choice = mainMenu.getInput()
    print(choice)