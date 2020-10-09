class Father:
    def __init__(self):
        self.name = '张三'
        self.__age = 30
    def sayHello(self):
        print(self.__age)
        print('你好')
    def __func(self):
        print('私有的方法')

class Son(Father):
    def haha(self):
        # 访问父类的私有属性和私有方法
        # print(self.__age)  # 父类私有成员+函数不能被子类访问 __age
        # self.__func()  # 父类私有成员+函数不能被子类访问  __func
        pass


father = Father()
father.sayHello()
# 私有成员+函数不能被对象访问
# father.__func()  # unresolved attribute reference __func for class Father

son = Son()
# print(son.name)
# # print(son.__age)
# son.sayHello()
son.sayHello()  # 子类可以通过调用继承的父类的方法访问父类的私有成员
son.haha()

# """-------------------------   -------------------------"""
"""------------------------- ok -------------------------"""