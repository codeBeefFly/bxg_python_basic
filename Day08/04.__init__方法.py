class Robot:
    def __init__(self,name):
        print('执行了init方法')
        self.name = name

# 创建对象
# 对象创建的时候,会自动调用__init__方法
# __init__方法相当于构造方法
root = Robot('李四')
robot1 = Robot('王五')