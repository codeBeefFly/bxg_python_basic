"""
需求：
1.游戏枪支有不同的型号,并拥有不同的伤害
2.枪支可以添加一定数量的子弹
3.枪支可以设计敌人,设计敌人时,如果子弹数量为0,则提示玩家;如果有子弹,会减少子弹,如果击中敌人,会让敌人受伤
4.输出枪支信息时,可以显示枪支的型号、伤害、子弹数量
5.游戏玩家分为警察和土匪两种角色,玩家拥有自己的枪支和血量,可以攻击敌人
6.玩家攻击敌人时,如果没有枪,则提示玩家;如果有枪,则检查枪支是否有子弹,有子弹则使用枪支射击敌人,没有子弹则自动给枪支添加子弹
7.玩家被击中会受伤,减少血量为枪支的伤害,提示玩家受伤并显示当前血量;如果血量<=0,则提示玩家死亡
8.输出玩家信息时,可以显示玩家角色、状态、血量、所持有枪支的信息
"""

'''---------------------- 枪支类 ----------------------'''
class Gun:
    def __init__(self,model,damage):
        # 型号
        self.model = model
        # 伤害
        self.damage = damage
        # 子弹数量
        self.bullet_count = 0

    def __str__(self):
        return '型号:{},伤害:{},子弹数量:{}'.format(self.model,self.damage,self.bullet_count)

    def add_bullet(self,count):
        '''
        添加子弹
        :param count:
        :return:
        '''
        self.bullet_count+=count

    def shoot(self,enemy):
        '''
        射击敌人
        :param enemy:玩家类型
        :return:
        '''
        # 判断子弹数量(不需要判断,因为玩家已经判断了)
        # 减少子弹
        self.bullet_count -= 1
        # 认为百分百击中,让敌人受伤
        enemy.hurt(self)



'''---------------------- 玩家类 ----------------------'''
from enum import Enum
class Role(Enum):
    POLICEMAN = '警察'
    BANDIT = '土匪'


class Player:
    def __init__(self,role,name):
        '''
        初始化
        :param role:角色名称
        :param name: 名字
        '''
        # 角色
        self.role = role
        # 名字
        self.name = name
        # 血量
        self.hp = 100
        # 枪支
        self.gun = None
        # 是否存活
        self.alive = True

    def __str__(self):
        return '角色:{},状态:{},血量:{},枪支:{}'.format(self.role,self.alive,self.hp,self.gun)

    def fire(self,enemy):
        '''
        攻击玩家
        :param enemy:玩家对象
        :return:
        '''
        # 判断是否有枪
        if not self.gun:
            # 没有枪
            print('没有枪,不能射击')
            return
        # 没有子弹
        if self.gun.bullet_count==0:
            print('没有子弹')
            self.gun.add_bullet(5)
            return
        # 有子弹,射击敌人
        self.gun.shoot(enemy)

    def hurt(self,enemy_gun):
        '''
        受到伤害
        :param enemy_gun:枪支对象
        :return:
        '''
        # 减少血量为枪支的伤害
        self.hp -= enemy_gun.damage

        print('玩家受伤,当前血量:{}'.format(self.hp))
        # 如果血量<=0 玩家死亡
        if self.hp<=0:
            print('玩家死亡')
            # 玩家死亡状态
            self.alive = False

'''---------------------- 程序流程 ----------------------'''
# 玩家
player1 = Player('警察','刘建明')
player2 = Player('土匪','陈永仁')
# 枪支
gun = Gun('AK47',10)
# print(gun)
# gun.add_bullet(5)
# print(gun)
# gun.shoot(player1)
# print(gun)
# print(player1)
# 把枪交给警察
player1.gun = gun
# 循环消灭匪徒
while True:
    player1.fire(player2)
    print(player2)
    if not player2.alive:
        break

# hello

