class Robot:
    def __init__(self, name, type):
        self.name = name
        self.type = type

    # 可以提取对象的特征(属性),输出对象的时候,会输出当前方法的返回值
    def __str__(self):
        return '名字:{},型号:{}'.format(self.name,self.type)


# 创建机器人对象
robot1 = Robot('ur机器人', 'ur5')
robot2 = Robot('AuBo机器人', 'AuBo i3')
# 打印这两个机器人对象
print(robot1)
print(robot2)
