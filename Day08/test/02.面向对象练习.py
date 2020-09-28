'''
定义一个表示学生信息的类Student要求如下：
(1)类Student的成员属性：sNO表示学号；sName表示姓名；sSex表示性别；sAge表示年龄；sPython：表示Python课程成绩。
(2)类Student的方法成员：getNo（）：获得学号；getName（）：获得姓名；getSex（）：获得性别；getAge（）获得年龄；getPython（）：获得Python 课程成绩
(3)根据类Student的定义，创建五个该类的对象，并定义容器保存5个学生对象 [stu1,stu2,stu3,stu4,stu5]
(4)计算并输出这五个学生Python语言成绩的平均值，

'''
import random
class Student:
    def __init__(self,sNo,sName,sSex,sAge,sPython):
        # (1)类Student的成员属性：sNO表示学号；sName表示姓名；sSex表示性别；sAge表示年龄；sPython：表示Python课程成绩。
        self.sNo = sNo
        self.sName = sName
        self.sSex = sSex
        self.sAge = sAge
        self.sPython = sPython
    # (2)类Student的方法成员：getNo（）：获得学号；getName（）：获得姓名；getSex（）：获得性别；getAge（）获得年龄；getPython（）：获得Python 课程成绩
    def getNo(self):
        return self.sNo

    def getName(self):
        return self.sName

    def getSex(self):
        return self.sSex

    def getAge(self):
        return self.sAge

    def getPython(self):
        return self.sPython


# (3)根据类Student的定义，创建五个该类的对象，并定义容器保存5个学生对象 [stu1,stu2,stu3,stu4,stu5]
names = ['张三','李四','王五','赵六']
sexs = ['男','女']
students = []
for index in range(5):
    a = random.randint(0,len(names)-1)
    name = names[a]

    b = random.randint(0,len(sexs)-1)
    sex = sexs[b]
    stu = Student(index,name,sex,random.randint(20,30),random.randint(40,99))
    # 添加到容器中
    students.append(stu)

for stu in students:
    print(stu.sName,stu.sPython)
# (4)计算并输出这五个学生Python语言成绩的平均值，
count = 0
for stu in students:
    count += stu.getPython()
# 求平均值
ava = count/len(students)
print(ava)

