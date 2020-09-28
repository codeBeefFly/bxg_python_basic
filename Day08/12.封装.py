'''---------------------- 洗衣机生产厂商 ----------------------'''
class WashMachine:
    def __init__(self,brand,capacity):
        # 品牌
        self.__brand = brand
        # 容量
        self.__capacity = capacity
        # 是否洗衣机门已经关闭
        self.__hasClosed = False
        # 模式  0:默认模式  1:轻柔模式 (洗内衣)  2:狂揉模式(外套)
        self.__mode = 0
        # 马达转速
        self.__motorSpeed = 0

    def openDoor(self):
        '''
        开洗衣机门
        :return:
        '''
        print('开洗衣机门')
        # 修改关闭洗衣机门的标志位
        self.__hasClosed = False

    def closeDoor(self):
        '''
        关洗衣机门
        :return:
        '''
        print('关闭洗衣机门')
        # 修改关闭洗衣机门的标志位
        self.__hasClosed = True

    def setMode(self,mode):
        '''
        设置模式
        :param mode 模式设置
        :return:
        '''
        if mode !=1 and mode!=2:
            print('设置模式错误')
            return

        if mode==1:
            # 调节马达转速
            self.__setMotorSpeed(1000)
        elif mode==2:
            self.__setMotorSpeed(2000)
        # 修改模式
        self.__mode = mode

    def __setMotorSpeed(self,speed):
        '''
        调节马达转速
        :param speed:
        :return:
        '''
        self.__motorSpeed = speed

    def start(self):
        '''
        开始洗衣服
        :return:
        '''
        # 必须要关闭洗衣机门才能开始洗衣服
        if not self.__hasClosed:
            print('请关闭洗衣机门,再开始洗衣服')
            return
        if self.__mode==0:
            print('请设置模式')
            return
        if self.__mode==1:
            print('开始放水...')
            print('水放满了...')
            print('轻柔模式...')
            print('马达转速:{}'.format(self.__motorSpeed))
            print('洗衣服...')
        elif self.__mode==2:
            print('开始放水...')
            print('水放满了...')
            print('狂揉模式...')
            print('马达转速:{}'.format(self.__motorSpeed))
            print('洗衣服...')


'''---------------------- 消费者 ----------------------'''
# 买一台洗衣机
washMachine = WashMachine('海尔',10)
# washMachine.brand = '小天鹅'
# 开始洗衣服
washMachine.openDoor()
print('放入衣服')
# 关闭洗衣机门
washMachine.closeDoor()
# washMachine.hasClosed = True
# 设置模式
washMachine.setMode(2)
# 调节马达转速
washMachine.__setMotorSpeed(5000)
# 开始洗衣服
washMachine.start()
