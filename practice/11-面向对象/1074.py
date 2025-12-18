# 题目描述
# 考试题目有普通题目、单选题目和多选题目。
# 普通题目Question对象可以通过setText方法设置题目描述文本，通过setAnswer方法设置答案，
# 调用print(Question对象)时显示题目描述文本，checkAnswer方法检查回答是否正确（直接比对回答与答案是否一致）。
# 测试程序程序如下：
"""
if __name__ == "__main__":
    q = Question()
    text = input()              # 输入题目描述
    answer = input()            # 输入题目答案
    q.setText(text)
    q.setAnswer(answer)
    print(q)
    respone = input()           # 输入回答
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

if __name__ == "__main__":
    q = Question()
    text = input()
    answer = input()
    q.setText(text)
    q.setAnswer(answer)
    print(q)
    response = input()
    print(q.checkAnswer(response))