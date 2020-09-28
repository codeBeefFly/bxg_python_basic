'''---------------------- 家具类 ----------------------'''
class Item:
    def __init__(self,type,area):
        # 家具类型
        self.type = type
        # 家具面积
        self.area = area

    def __str__(self):
        return '家具类型:{},家具面积:{}'.format(self.type,self.area)

'''---------------------- 房子类 ----------------------'''
class Home:
    def __init__(self,address,area):
        # 房子地址
        self.address = address
        # 房子面积
        self.area = area
        # 剩余面积
        self.free_area = self.area
        # 家具列表
        self.items = []

    def __str__(self):
        return '地址:{},面积:{},剩余面积:{}'.format(self.address,self.area,self.free_area)

    def add_item(self,item):
        '''
        添加家具
        :param item: Item家具类型
        :return:
        '''
        if self.free_area>=item.area:
            # 减少剩余面积
            self.free_area -= item.area
            # 将家具添加到家具列表中
            self.items.append(item)
            # 如果可以容纳,添加成功
            print('添加成功')
        else:
            # 否则,添加失败
            print('添加失败')


# 创建家具类
item = Item('桌子',4)
# 创建房子
house = Home('深圳湾一号',140)
# 输出家具和房子
print('家具',item)
print('房子',house)
print('家具个数',len(house.items))
# 添加家具
house.add_item(item)
print('添加之后的房子',house)
print('添加之后家具个数',len(house.items))


