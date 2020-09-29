"""------------------------- 枪械类 -------------------------"""


class Gun:

    def __init__(self, name, damage):
        self.name = name
        self.damage = int(damage)
        self.bullets = 0

    def __str__(self):
        return '枪支信息：名称[{}]，伤害值[{}]，弹药量[{}]'.format(self.name, self.damage, self.bullets)

    def add_bullets(self, new_bullets):
        """
        添加子弹
        :param new_bullets: 新的子弹数量
        :return: None
        """
        self.bullets += new_bullets
        print('添加了[{}]弹药，剩余弹药[{}]'.format(new_bullets, self.bullets))

    def shoot(self, target):
        """
        对目标进行射击，目标是 player 类对象
        :param target: player类对象
        :return: None
        """
        self.bullets -= 1
        target.get_hurt(self)


"""------------------------- 玩家类 -------------------------"""
from enum import Enum


class Role(Enum):
    counter_terrorist = '反恐精英'
    terrorist = '恐怖分子'


class Player:

    def __init__(self, role, name, hp=100):
        self.role = role
        self.name = name
        self.hp = hp
        self.gun = None  # 接收 Gun 类型对象
        self.is_alive = True

    def __str__(self):
        return '玩家信息：名字[{}]，角色[{}]，生命值[{}]，存活[{}]'.format(self.name, self.role, self.hp, self.is_alive)

    def grab_gun(self, gun):
        self.gun = gun
        print('捡起一把武器[{}]'.format(gun.name))

    def fire_at(self, target):
        """
        对目标射击，默认只射击目标
        :param target: Player 类对象
        :return:
        """
        if not self.gun:
            print('没有武器')
            return
        if self.gun.bullets == 0:
            print('弹药为0，添加5个弹药')
            self.gun.add_bullets(5)
        self.gun.shoot(target)

    def get_hurt(self, gun):
        """
        目标对象受到枪支伤害
        :param gun: Gun 类型对象
        :return:
        """
        self.hp -= gun.damage

        if self.hp <= 0:
            self.is_alive = False
            print('玩家[{}]，角色[{}]，受到攻击!，当前血量[{}]，状态[{}]，持枪[{}]'.format(self.name, self.role, self.hp, self.is_alive, self.gun))
            return
        print('玩家[{}]，角色[{}]，受到攻击!，当前血量[{}]，状态[{}]，持枪[{}]'.format(self.name, self.role, self.hp, self.is_alive, self.gun))



def test_gun():
    ak_47 = Gun('AK-47', 20)
    print(ak_47)


def test_game():
    player_1 = Player('反恐精英', 'jacob')
    player_2 = Player('恐怖分子', 'king')

    print(player_1, '\n', player_2)

    ak_47 = Gun('AK-47', '20')
    bullets = 30
    player_2.grab_gun(ak_47)
    ak_47.add_bullets(bullets)
    while True:
        player_2.fire_at(player_1)
        if not player_1.is_alive:
            break



if __name__ == '__main__':
    test_game()
