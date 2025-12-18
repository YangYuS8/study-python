# 题目描述
# 继承考试题目类Question设计单选题目类ChoiceQuestion。
# ChoiceQuestion类有addChoice(choice, correct)方法用来添加一个选项，
# 其中choice是需要添加的选项，correct表示该选项是否是正确选项，addChoice方法中根据correct自动更新题目答案。
# print(ChoiceQustion对象)时，除了输出题目描述文本外，还要输出各个答案选项。
# 测试程序如下：
"""
if __name__ == "__main__":
    q = ChoiceQuestion()
    text = input()              # 输入题目描述
    q.setText(text)
    for i in range(4):
        choice, correct = input().split()   #输入一个选项以及该选项是否是正确答案
        correct = eval(correct)
        q.addChoice(choice, correct)
    print(q)                    # 输出题目描述及所有选项
    respone = input()           # 输入回答选项编号
    print(q.checkAnswer(respone))
"""
class Question:
    def __init__(self):
        self.text = ""
        self.answer = ""

    def setText(self, text):
        self.text = text

    def setAnswer(self, answer):
        self.answer = answer

    def __str__(self):
        return self.text

    def checkAnswer(self, response):
        return response == self.answer

class ChoiceQuestion(Question):
    def __init__(self):
        super().__init__()
        self.choices = []

    def addChoice(self, choice, correct):
        self.choices.append(choice)
        if correct:
            self.setAnswer(str(len(self.choices)))

    def __str__(self):
        result = self.text + "\n"
        for i, choice in enumerate(self.choices, 1):
            result += f"{i}:{choice}\n"
        return result

if __name__ == "__main__":
    q = ChoiceQuestion()
    text = input()
    q.setText(text)
    for i in range(4):
        parts = input().split()
        choice = parts[0]
        correct = eval(parts[1])
        q.addChoice(choice, correct)
    print(q, end='')
    response = input()
    print(q.checkAnswer(response))