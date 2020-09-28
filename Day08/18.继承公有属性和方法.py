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
        # print(self.__age)
        self.__func()

son = Son()
# print(son.name)
# # print(son.__age)
# son.sayHello()
son.haha()