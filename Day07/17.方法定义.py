# 定义机器人类
def func():
    print('函数')
class Robot:
    def movej(self,joints):
        # self参数 调用时 不用传递
        # 除了self参数之外的参数都需要传递
        print('关节移动')

    def movel(self):
        print('直线移动')

# 创建对象
robot = Robot()
# 调用  需要通过对象来调用
robot.movej([1,2,3,4,5,6])
# robot.movel()
