class Circle:
    def __init__(self, radius):
        # 半径
        self.radius = radius
        # 圆周率(圆周率不能在外部修改)
        self.__PI = 3.1415926

    def getPI(self):
        return self.__PI

    def perimeter(self):
        return 2 * self.__PI * self.radius


# 创建圆
circle = Circle(20)
# 访问内部的__PI 如何做?
# circle.__PI = 40
print(circle.getPI())


# print(circle.__PI)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def getAge(self):
        '''
        获取age属性
        :return:
        '''
        return self.__age

    def setAge(self,age):
        if age>0 and age<150:
            self.__age = age
        else:
            print('不合法')

    def __str__(self):
        return '姓名:{},年纪:{}'.format(self.name,self.__age)

person = Person('张三', 30)
# 修改年纪
# 获取年纪
print(person.getAge())
# 修改年纪
person.setAge(-100)
print(person.getAge())

