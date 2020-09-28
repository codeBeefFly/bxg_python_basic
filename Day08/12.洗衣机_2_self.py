"""
需求：
创建一个洗衣机类，并实现面向对象功能

需要进行2-3次迭代，可以根据迭代创建多个.py文件
第一次迭代（本次迭代）
在洗衣机类内部实现基本的功能
属性
1. 洗衣机品牌
2. 洗衣机容量
功能
1. 打开门
2. 关闭门
3. 开始洗衣服
第二次迭代，对属性进行私有化处理
增加
1. 私有化标签变量 __hasClosed
2. 私有化模式变量 __mode(0, 1, 2)
增加
1. 私有化函数
修改逻辑
增加
1. 设置模式

"""

class Washing_Machine:

    def __init__(self, brand, capacity):
        self.__brand = brand  # 不能让外部修改
        self.__capacity = capacity  # 不能让外部修改
        self.__has_closed = False
        self.__mode = 0
        self.__motor_speed = 0

    def __str__(self):
        print('洗衣机品牌[{}]，容积[{}]'.format(self.__brand, self.__capacity))

    def __set_motor_speed(self, speed):
        self.__motor_speed = speed

    def open_door(self):
        print('打开洗衣机盖子')
        self.__has_closed = False

    def close_door(self):
        print('关闭洗衣机盖子')
        self.__has_closed = True

    def set_mode(self, input_mode):
        print('input_mode:: ', input_mode)
        if input_mode != 1 and input_mode != 2:
            print('设置模式错误')
            return
        elif self.__mode == 1:
            self.__set_motor_speed(1000)
        elif self.__mode == 2:
            self.__set_motor_speed(2000)
        # 设置模式
        self.__mode = input_mode

    def start(self):
        # if self.__has_closed:
        #     print('开始洗衣服')
        #     print('开始放水')
        #     print('水放满了')
        #     print('洗衣服ing...')
        #     self.stop()
        # print('请关闭洗衣机盖儿')
        # return
        # 判断是否盖盖儿
        if not self.__has_closed:
            print('请关闭洗衣机盖儿')
            return  # 中断操作
        # 如果盖盖儿，判断mode
        if self.__mode == 0:
            print('请选择模式')
            return
        elif self.__mode == 1:
            print('开始放水...')
            print('水放满了...')
            print('轻柔模式...')
            print('马达转速:{}'.format(self.__motor_speed))
            print('洗衣服...')
        elif self.__mode == 2:
            print('开始放水...')
            print('水放满了...')
            print('狂暴模式...')
            print('马达转速:{}'.format(self.__motor_speed))
            print('洗衣服...')

    def stop(self):
        print('结束')


if __name__ == '__main__':
    washing_machine_haier = Washing_Machine('海尔', 50)
    # 打开机盖
    washing_machine_haier.open_door()
    # 关闭机盖
    washing_machine_haier.close_door()
    # 设置模式
    washing_machine_haier.set_mode(2)
    # 开始洗衣
    washing_machine_haier.start()