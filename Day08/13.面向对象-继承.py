'''
1.定义人类,具有name和age属性,具有sayHello方法
2.定义学生类,具有name和age属性,具有study方法和打招呼sayHello方法
3.定义老师类,具有name和age属性,具有teach方法和打招呼sayHello方法

'''
# 1.定义人类,具有name和age属性,具有sayHello方法
class Person:
    def __init__(self,name,age):
        # 姓名
        self.name = name
        # 年纪
        self.age = age

    def sayHello(self):
        print('你好')

# 2.定义学生类,具有name和age属性,具有study方法和打招呼sayHello方法
class Student(Person):
    # def __init__(self,name,age):
    #     # 姓名
    #     self.name = name
    #     # 年纪
    #     self.age = age

    # def sayHello(self):
    #     print('你好')

    def study(self):
        print('学习')


# 3.定义老师类,具有name和age属性,具有teach方法和打招呼sayHello方法
class Teacher(Person):
    # def __init__(self, name, age):
    #     # 姓名
    #     self.name = name
    #     # 年纪
    #     self.age = age
    #
    # def sayHello(self):
    #     print('你好')

    def teach(self):
        print('教学')

# 学生对象
stu = Student('小明',30)
print(stu.name)
print(stu.age)
stu.sayHello()
# 老师对象
# tea = Student('小王',50)



