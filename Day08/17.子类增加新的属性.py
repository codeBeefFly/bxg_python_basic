'''
如果继承,没有实现__init__方法,调用的是父类的__init__方法
一旦子类定义了__init__方法,父类的__init__方法就不再执行了
'''

class Robot:
    def __init__(self,name):
        self.name  = name

# UR机器人
class URRobot(Robot):
    def __init__(self,name,type):
        # 调用父类的init方法,把参数传递过去
        super(URRobot, self).__init__(name)
        # 增加的属性
        self.type = type

urrobot = URRobot('UR机器人','UR3')
print(urrobot.type)
print(urrobot.name)