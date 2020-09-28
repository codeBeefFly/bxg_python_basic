class Robot:
    def __motor(self):
        '''
        驱动电机转动
        :return:
        '''
        print('驱动伺服电机转动')

    def movej(self):
        print('开始关节移动')

# 创建机器人
robot = Robot()
# robot.movej()
robot.__motor()