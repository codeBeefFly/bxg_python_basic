'''
分析:
1.移动机器人到放松姿势
2.点头 抬头 做100次
'''
from sdk.ur import UR

# 创建机器人驱动
ur = UR()
# 连接机器人
ur.connect()
# 移动到放松的姿势
ur.move_j([-90,-101.50,-77.50,-13.50,91.50,0])
# 点头点的位 置和姿态
downPos = [-0.107,-0.57773,0.38707,-102.49585,0.32462,-178.53554]
ur.move_l(downPos)
# 控制点头和抬头100次
for index in range(1,100):
        if index%2==0:
            # 向下
            downPos[2]-=0.4
            ur.move_l(downPos, v=1)
        else:
            # 向上
            downPos[2]+=0.4
            ur.move_l(downPos, v=1)
