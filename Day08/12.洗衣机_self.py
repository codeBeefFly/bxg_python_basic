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
"""

class Washing_Machine:

    def __init__(self, brand, capacity):
        self.brand = brand  # 不能让外部修改
        self.capacity = capacity  # 不能让外部修改

    def __str__(self):
        print('洗衣机品牌[{}]，容积[{}]'.format(self.brand, self.capacity))

    def open_door(self):
        print('打开洗衣机盖子')

    def close_door(self):
        print('关闭洗衣机盖子')

    def start(self):
        print('开始洗衣服')
        print('开始放水')
        print('水放满了')
        print('洗衣服ing...')

        self.stop()

    def stop(self):
        print('结束')


if __name__ == '__main__':
    washing_machine_haier = Washing_Machine('海尔', 50)
    # 打开机盖
    washing_machine_haier.open_door()
    # 关闭机盖
    washing_machine_haier.close_door()
    # 开始洗衣
    washing_machine_haier.start()