'''
手机电量默认是100
	打游戏每次消耗电量10
	听歌每次消耗电量5
	打电话每次消耗电量4
	接电话每次消耗电量3
	充电可以为手机补充电量

'''
class Phone:
    def __init__(self):
        # 手机电量默认是100
        self.battery = 100

    # 打游戏每次消耗电量10
    def playGame(self):
        if self.battery<10:
            print('电量不足,请充电')
            return

        self.battery -= 10
    # 听歌每次消耗电量5
    def listenMusic(self):
        if self.battery<5:
            print('电量不足,请充电')
            return
        self.battery -=5
    # 打电话每次消耗电量4
    def call(self):
        if self.battery<4:
            print('电量不足,请充电')
            return
        self.battery-=4
    # 接电话每次消耗电量3
    def reciveCall(self):
        if self.battery<3:
            print('电量不足,请充电')
            return
        self.battery -=3
    # 充电可以为手机补充电量
    def charge(self,battery):
        '''
        根据功率充电
        :param battery:
        :return:
        '''

        self.battery += battery
        if self.battery>=100:
            print('充满了')
            self.battery = 100


    def __str__(self):
        return '手机电量:{}'.format(self.battery)

# 创建手机
phone = Phone()
print(phone)
phone.playGame()
phone.playGame()
phone.playGame()
phone.playGame()
phone.playGame()
phone.playGame()
phone.playGame()
phone.playGame()
phone.playGame()
phone.playGame()
print(phone)
phone.listenMusic()
print(phone)





