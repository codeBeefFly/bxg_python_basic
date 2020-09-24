"""
1. 从控制台输入要出的拳 —— 石头（1）／剪刀（2）／布（3）
2. 电脑 随机 出拳 -- 先假定电脑出石头
3. 比较胜负
"""
# # 1. 从控制台输入要出的拳 —— 石头（1）／剪刀（2）／布（3）
# person = int(input('请输入你的出拳'))
# # 2. 电脑 随机 出拳 -- 先假定电脑出石头
# computer = 1
# # 3. 比较胜负
# if (person==1 and computer==2) or (person==2 and computer==3) or (person==3 and computer==1):
#     print('玩家:{},电脑:{},玩家胜利'.format(person,computer))
# elif person==computer:
#     print('玩家:{},电脑:{},平局'.format(person,computer))
# else:
#     print('玩家:{},电脑:{},电脑胜利'.format(person,computer))

# 只需要把python写好的功能导入过来直接使用即可
import random
# 1. 从控制台输入要出的拳 —— 石头（1）／剪刀（2）／布（3）
# quit_flag = True
while True:
    person = int(input('请输入你的出拳'))
    # 2. 电脑 随机 出拳 -- 先假定电脑出石头
    computer = random.randint(1,3) # 1 2 3
    # 3. 比较胜负
    if (person==1 and computer==2) or (person==2 and computer==3) or (person==3 and computer==1):
        print('玩家:{},电脑:{},玩家胜利'.format(person,computer))
        continue
    elif person==computer:
        print('玩家:{},电脑:{},平局'.format(person,computer))
        continue
    elif (person != 1 and person != 2 and person !=3 ):
        # 如果没有按规矩出牌，退出
        print('玩家没有正常出牌，退出...')
        break
    else :
        print('玩家:{},电脑:{},电脑胜利'.format(person,computer))
        continue
