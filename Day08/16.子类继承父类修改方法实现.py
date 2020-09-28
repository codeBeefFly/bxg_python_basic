'''
1.定义父类,具有sayHello方法
2.子类继承父类,修改sayHello方法

'''
# 1.定义父类,具有sayHello方法
class Father:
    def sayHello(self):
        print('同志好')

# 2.子类继承父类,修改sayHello方法
class Son(Father):
    def sayHello(self):
        print('美女你好')

# 创建Son对象
son = Son()
# 调用sayHello方法
son.sayHello()