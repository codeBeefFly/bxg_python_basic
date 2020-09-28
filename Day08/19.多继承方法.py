'''
定义Mother类,Mother具有cook方法
定义Father类,Father具有makeMoney方法

'''

'''
多继承可以使用多个父类中定义的公有方法
'''

# 定义Mother类,Mother具有cook方法
class Mother:
    def cook(self):
        print('做饭')


# 定义Father类,Father具有makeMoney方法
class Father:
    def makeMoney(self):
        print('赚钱')


# 子类
class Son(Mother, Father):
    def cook(self):
        print('做炒饭')


# 创建子类对象
son = Son()
son.cook()
son.makeMoney()
