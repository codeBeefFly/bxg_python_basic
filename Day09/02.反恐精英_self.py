"""
需求：
5.游戏玩家分为警察和土匪两种角色,玩家拥有自己的枪支和血量,可以攻击敌人
6.玩家攻击敌人时,如果没有枪,则提示玩家;
    如果有枪,则检查枪支是否有子弹,有子弹则使用枪支射击敌人,
    没有子弹则自动给枪支添加子弹
7.玩家被击中会受伤,减少血量为枪支的伤害,提示玩家受伤并显示当前血量;
    如果血量<=0,则提示玩家死亡
8.输出玩家信息时,可以显示玩家角色、状态、血量、所持有枪支的信息
"""

"""------------------------- 枪支类 -------------------------"""
# 1.游戏枪支有不同的型号,并拥有不同的伤害
# 2.枪支可以添加一定数量的子弹
# 3.枪支可以设计敌人,设计敌人时,如果子弹数量为0,则提示玩家;
#     如果有子弹,会减少子弹,如果击中敌人,会让敌人受伤
# 4.输出枪支信息时,可以显示枪支的型号、伤害、子弹数量
class Gun:
    def __init__(self, model, damage):
        self.model = model
        self.damage = damage
        self.bullet_count = 0

    def __str__(self):
        return '型号[{}], 伤害[{}], 子弹数量[{}]'.format(self.model, self.damage, self.bullet_count)

    def add_bullet(self, new_bullet):
        self.bullet_count += new_bullet

    def shoot(self, enemy):
        self.bullet_count -= 1
        enemy.hurt(self)

"""------------------------- 玩家类 -------------------------"""

"""------------------------- 机器人 -------------------------"""
# class Bot:
#     def __init__(self):
#         self.life_point = 100
#
#     def hurt(self):
#         pass
#
#     def fire(self, enemy):
#


def test_gun():
    ak_47 = Gun('AK-47', 20)
    ak_47.add_bullet(30)
    pass


if __name__ == '__main__':
    pass