# 题目描述
# 课程包括理论课和实验课两种类型。为此设计一个抽象基类课程Course，然后派生理论课TheoryCourse和实验课LabCourse两个子类。
# Course类的__init__方法初始化课程代码、课程名、授课教师；
# enroll_students方法用于学生选课，为该课程添加一组学生学号；
# drop_students方法用于学生退课，为该课程删除一组学生学号；
# get_students方法返回所有学生学号组成的字符串；
# upload_grades方法用于上传所有学生成绩，成绩有两个部分构成；
# calculate_grades是一个抽象方法，用于计算并返回成绩（四舍五入）；
# get_course_type是一个抽象方法，用于返回课程类型。
# TheoryCourse子类实现upload_grades和calculate_grades方法，理论课程成绩包括作业和考试两个部分构成，权重分别为40%和60%。
# get_course_type方法返回'理论课'
# LabCourse子类实现upload_grades和calculate_grades方法，实验课程成绩包括实验报告和实验操作两个部分构成，权重分别为70%和30%。
# get_course_type方法返回'实验课'。
# 程序如下：
"""
from abc import ABC, abstractmethod
class Course(ABC):
    # 课程抽象基类
    def __init__(self, course_code, course_name, instructor):
        self.course_code = course_code
        self.course_name = course_name
        self.instructor = instructor
        self.enrolled_students = []
        self.scores1 = None
        self.scores2 = None
    def __str__(self):
        return ' '.join([self.course_code, self.course_name, self.instructor, self.get_course_type()])
if __name__ == "__main__":
    line1 = input().split()
    line2 = input().split()
    theory = TheoryCourse(*line1)
    lab = LabCourse(*line2)
    # 输出课程信息
    print(theory)
    print(lab)
    thestu1 = input().split()
    thestu2 = input().split()
    thestu3 = input().split()
    theory.enroll_students(thestu1)
    theory.enroll_students(thestu2)
    theory.drop_students(thestu3)
    labstu1 = input().split()
    labstu2 = input().split()
    labstu3 = input().split()
    lab.enroll_students(labstu1)
    lab.enroll_students(labstu2)
    lab.drop_students(labstu3)
    # 输出学生学号
    print(theory.get_students())
    print(lab.get_students())
    thescore1 = map(int, input().split())
    thescore2 = map(int, input().split())
    theory.upload_grades(list(thescore1), list(thescore2))
    labscore1 = map(int, input().split())
    labscore2 = map(int, input().split())
    lab.upload_grades(list(labscore1), list(labscore2))
    # 输出成绩
    print(theory.calculate_grades())
    print(lab.calculate_grades())
"""
from abc import ABC, abstractmethod

class Course(ABC):
    """课程抽象基类"""

    def __init__(self, course_code, course_name, instructor):
        self.course_code = course_code
        self.course_name = course_name
        self.instructor = instructor
        self.enrolled_students = []
        self.scores1 = None
        self.scores2 = None

    def enroll_students(self, students):
        """为学生选课，添加一组学生学号"""
        for student in students:
            if student not in self.enrolled_students:
                self.enrolled_students.append(student)

    def drop_students(self, students):
        """学生退课，删除一组学生学号"""
        for student in students:
            if student in self.enrolled_students:
                self.enrolled_students.remove(student)

    def get_students(self):
        """返回所有学生学号组成的字符串，用空格分隔"""
        return ' '.join(self.enrolled_students)

    def upload_grades(self, scores1, scores2):
        """上传所有学生成绩，成绩有两个部分构成"""
        self.scores1 = scores1
        self.scores2 = scores2

    @abstractmethod
    def calculate_grades(self):
        """计算并返回成绩（四舍五入），返回列表形式"""
        pass

    @abstractmethod
    def get_course_type(self):
        """返回课程类型"""
        pass

    def __str__(self):
        return ' '.join([self.course_code, self.course_name, self.instructor, self.get_course_type()])

class TheoryCourse(Course):
    def get_course_type(self):
        return '理论课'

    def calculate_grades(self):
        # 理论课程成绩：作业(40%) + 考试(60%)
        if self.scores1 is None or self.scores2 is None:
            return []
        grades = []
        for s1, s2 in zip(self.scores1, self.scores2):
            # 计算加权成绩并四舍五入
            final_grade = round(s1 * 0.4 + s2 * 0.6)
            grades.append(final_grade)
        return grades

class LabCourse(Course):
    def get_course_type(self):
        return '实验课'

    def calculate_grades(self):
        # 实验课程成绩：实验报告(70%) + 实验操作(30%)
        if self.scores1 is None or self.scores2 is None:
            return []
        grades = []
        for s1, s2 in zip(self.scores1, self.scores2):
            # 计算加权成绩并四舍五入
            final_grade = round(s1 * 0.7 + s2 * 0.3)
            grades.append(final_grade)
        return grades

if __name__ == "__main__":
    line1 = input().split()
    line2 = input().split()
    theory = TheoryCourse(*line1)
    lab = LabCourse(*line2)
    # 输出课程信息
    print(theory)
    print(lab)
    thestu1 = input().split()
    thestu2 = input().split()
    thestu3 = input().split()
    theory.enroll_students(thestu1)
    theory.enroll_students(thestu2)
    theory.drop_students(thestu3)
    labstu1 = input().split()
    labstu2 = input().split()
    labstu3 = input().split()
    lab.enroll_students(labstu1)
    lab.enroll_students(labstu2)
    lab.drop_students(labstu3)
    # 输出学生学号
    print(theory.get_students())
    print(lab.get_students())
    thescore1 = list(map(int, input().split()))
    thescore2 = list(map(int, input().split()))
    theory.upload_grades(thescore1, thescore2)
    labscore1 = list(map(int, input().split()))
    labscore2 = list(map(int, input().split()))
    lab.upload_grades(labscore1, labscore2)
    # 输出成绩
    print(theory.calculate_grades())
    print(lab.calculate_grades())