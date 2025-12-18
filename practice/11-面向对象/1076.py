# 题目描述
# 继承考试题目类Question设计多选题目类MultiChoiceQuestion。
# MultiChoiceQuestion类有addChoice(choice, correct)方法用来添加一个选项，
# 其中choice是需要添加的选项，correct表示该选项是否是正确选项，addChoice方法中根据correct自动更新题目答案。
# print(MultiChoiceQuestion对象)时，除了输出题目描述文本外，还要输出各个答案选项，
# 并在题目描述文本后再输出一行“此题为多选题”。
# checkAnswer方法检查时既不多选也不少选才能判定为正确，且与回答顺序无关，比如答案是1和2，回答1 2或者2 1都应判定为正确。
# 测试程序如下：
"""
if __name__ == "__main__":
    q = MultiChoiceQuestion()
    text = input()              # 输入题目描述
    q.setText(text)
    for i in range(5):
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

class MultiChoiceQuestion(Question):
    def __init__(self):
        super().__init__()
        self.choices = []

    def addChoice(self, choice, correct):
        self.choices.append(choice)
        if correct:
            choice_num = len(self.choices)
            if self.answer == "":
                self.answer = str(choice_num)
            else:
                self.answer += " " + str(choice_num)

    def __str__(self):
        result = self.text + "\n"
        result += "此题为多选题\n"
        for i, choice in enumerate(self.choices, 1):
            result += f"{i}:{choice}\n"
        return result.rstrip("\n")

    def checkAnswer(self, response):
        ans_list = sorted(self.answer.split())
        resp_list = sorted(response.split())
        return ans_list == resp_list

if __name__ == "__main__":
    q = MultiChoiceQuestion()
    text = input()
    q.setText(text)
    for i in range(5):
        parts = input().split()
        # 选项可能有空格，所以需要特殊处理
        # 根据样例，选项和布尔值之间用多个空格分隔，所以我们可以这样处理：
        # 先找到最后一个空格，分割出布尔值
        line = " ".join(parts[:-1])  # 选项可能由多个单词组成
        correct = parts[-1]  # 最后一个部分是布尔值
        correct = eval(correct)
        q.addChoice(line, correct)
    print(q)
    response = input()
    print(q.checkAnswer(response))