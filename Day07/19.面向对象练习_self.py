'''
定义一个表示学生信息的类Student要求如下：
(1)类Student的成员属性：sNO表示学号；sName表示姓名；sSex表示性别；sAge表示年龄；sPython：表示Python课程成绩。
(2)类Student的方法成员：getNo（）：获得学号；getName（）：获得姓名；getSex（）：获得性别；getAge（）获得年龄；getPython（）：获得Python 课程成绩
(3)根据类Student的定义，创建五个该类的对象，并定义容器保存5个学生对象 [stu1,stu2,stu3,stu4,stu5]
(4)计算并输出这五个学生Python语言成绩的平均值，


'''

class Student:
    def __init__(self, sName='unknown', sNo = 'unknown', sSex='unknown', sAge=0, sPython=0):
        self.__sName = sName
        self.__sNo = sNo
        self.__sSex = sSex
        self.__sAge = sAge
        self.__sPython = sPython

    def getNo(self):
        """
        取得学生学号
        :return: 返回sNo
        """
        return self.__sNo

    def getName(self):
        """
        取得学生姓名
        :return: 返回sName
        """
        return self.__sName

    def getSex(self):
        """
        取得学生性别
        :return: 返回sSex
        """
        return self.__sSex

    def getAge(self):
        """
        取得学生年龄
        :return: 返回sAge
        """
        return self.__sAge

    def getPython(self):
        """
        取得学生成绩
        :return: 返回sPython
        """
        return self.__sPython


# if __name__ == '__main__':
def demo_01():
    # student_list = []

    stu_1 = Student('aaa', '001', 'm', 16, 80)
    stu_2 = Student('bbb', '002', 'm', 18, 70)
    stu_3 = Student('ccc', '003', 'm', 26, 75)
    stu_4 = Student('ddd', '004', 'm', 26, 90)
    stu_5 = Student('eee', '005', 'm', 20, 60)

    student_list = [stu_1, stu_2, stu_3, stu_4,stu_5]

    for i, student in enumerate(student_list):
        print('学生[{}]的信息'.format(i))
        print('姓名[{}], 学号[{}], 年龄[{}]，性别[{}]，成绩[{}]'.format(
            student.getName(), student.getNo(), student.getAge(),
            student.getSex(), student.getPython()
        ))

def demo_02():
    # 使用 random 和 for 对每一个学生赋值

    import random

    # 创建全局学生列表
    student_list = []
    # name, no, sex, gender, python
    name_list = ['aaa', 'bbb', 'ccc', 'ddd', 'eee']
    gender_list = ['male', 'female']
    # 循环添加学生到学生列表
    for i in range(1, 6):
        # 随机name
        name_max_index = len(name_list) - 1
        sName = name_list[random.randint(0, name_max_index)]  # randint(a, b) == randrange(a, b+1)
        name_max_index -= 1
        name_list.remove(sName)
        # 随机no
        sNo = str(random.randint(1, 5))
        # 随机sex
        sSex = gender_list[random.randint(0, len(gender_list)-1)]
        # 随机age
        sAge = random.randint(15, 30)
        # 随机python
        sPython = random.randint(20, 100)
        # 创建新学生对象
        new_student = Student(sName=sName, sNo=sNo, sSex=sSex, sAge=sAge, sPython=sPython)
        # 添加到学生列表
        student_list.append(new_student)

    # 打印学生信息
    for i, student in enumerate(student_list):
        print('学生[{}]的信息'.format(i))
        print('姓名[{}], 学号[{}], 年龄[{}]，性别[{}]，成绩[{}]'.format(
            student.getName(), student.getNo(), student.getAge(),
            student.getSex(), student.getPython()
        ))

    # 计算学生成绩平均值
    sPython_avg = 0
    for student in student_list:
        # sPython_avg += student.__sPython  # unresolved attribute reference to __sPython
        sPython_avg += student.getPython()  # unresolved attribute reference to __sPython
    sPython_avg = sPython_avg / 5
    print('学生成绩平均值为 {}'.format(sPython_avg))


if __name__ == '__main__':
    demo_02()
