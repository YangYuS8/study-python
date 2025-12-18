# 题目描述
# 设计一个邮件类Message和邮箱类Mailbox。每个邮件存储收件人、发件人和邮件正文信息。
# Message类提供方法如下：初始化方法__init__初始化邮件的收件人和发件人；
# append方法向邮件正文增加一行文本；toString方法将邮件生成一个长字符串的，
# 例如："From:张三\nTo:李四\n我们一起学习Python\n遇到问题相互交流，共同进步\n"。
# Mailbox类提供方法如下：添加一封邮件方法addMessage；
# 获取序号为index的邮件方法getMessage；删除序号为index的邮件方法delMessage。
# 测试程序如下：
"""
# if __name__ == "__main__":
#     myMail = MailBox()
#     n = int(input())
#     for i in range(n):
#         recipient, sender = input().split()   # 新增邮件收件人和发件人
#         message = Message(recipient, sender)
#         lineNumber = int(input())             # 邮件正文行数
#         for i in range(lineNumber):
#             text = input()
#             message.append(text)
#         myMail.addMessage(message)
#     idx = int(input())                        # 获取邮件index
#     message = myMail.getMessage(idx)
#     print(message.toString())
#     idx = int(input())                        # 删除邮件index
#     myMail.delMessage(idx)
#     for i in range(len(myMail)):              # 显示邮箱中所有邮件
#         message = myMail.getMessage(i)
#         print(message.toString())
"""
class Message:
    def __init__(self, recipient, sender):
        self.recipient = recipient
        self.sender = sender
        self.content = []

    def append(self, text):
        self.content.append(text)

    def toString(self):
        lines = [f"From:{self.sender}", f"To:{self.recipient}"]
        lines.extend(self.content)
        return '\n'.join(lines) + '\n'

class MailBox:
    def __init__(self):
        self.messages = []

    def addMessage(self, message):
        self.messages.append(message)

    def getMessage(self, index):
        return self.messages[index]

    def delMessage(self, index):
        del self.messages[index]

    def __len__(self):
        return len(self.messages)

if __name__ == "__main__":
    myMail = MailBox()
    n = int(input())
    for i in range(n):
        recipient, sender = input().split()
        message = Message(recipient, sender)
        lineNumber = int(input())
        for i in range(lineNumber):
            text = input()
            message.append(text)
        myMail.addMessage(message)
    idx = int(input())
    message = myMail.getMessage(idx)
    print(message.toString(), end='')
    idx = int(input())
    myMail.delMessage(idx)
    for i in range(len(myMail)):
        message = myMail.getMessage(i)
        print(message.toString(), end='')