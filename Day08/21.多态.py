'''---------------------- 父类 ----------------------'''
class Human:
    def eat(self):
        print('人类吃饭')

'''---------------------- 中国人 ----------------------'''
class ZhHuman(Human):
    def eat(self):
        print('用筷子吃饭')

'''---------------------- 美国人 ----------------------'''
class USHuman(Human):
    def eat(self):
        print('用刀叉吃饭')

'''---------------------- 非洲人 ----------------------'''
class AfricaHuman(Human):
    def eat(self):
        print('用手抓恩希玛')

'''---------------------- 狗 ----------------------'''
class Dog:
    def eat(self):
        print('狗啃骨头')

'''---------------------- 函数 ----------------------'''
# java c++静态类型语言 可以确定参数类型 Human
# python只要具备eat功能对象,都可以传递进去
def translate(human):
    '''
    传递一个具备吃饭功能的Human对象
    :param human: Human对象
    :return:
    '''
    human.eat()
    # human.makeMoney()

# 创建对象
# human = Human()
zhHuman = ZhHuman()
usHuman = USHuman()
afHuman = AfricaHuman()

# 调用函数
# translate(human)
# translate(zhHuman)
# translate(usHuman)
# translate(afHuman)

'''---------------------- 鸭子模型 ----------------------'''
# 创建Dog对象
dog = Dog()
translate(dog)
# translate(40)
# 动物:叫起来 像鸭子  跳起来像鸭子
# python认为是一个鸭子
# int a = 10
# a = 10