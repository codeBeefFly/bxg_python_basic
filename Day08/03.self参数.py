class Robot:
    def __init__(self,name):
        self.name = name
    
    def movej(self):
        print(self.name)
        print('开始关节移动')

# 创建对象
robot = Robot('ur机器人')
print('robot对象',robot)
# ur3 1 ur机器人 2
robot.movej()
robot.name = 'ur3'
# robot1 = Robot('ur机器人')
# print('robot1对象',robot1)
# robot1.movej()
print(vars(robot).items())
