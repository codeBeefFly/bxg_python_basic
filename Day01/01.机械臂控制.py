from sdk.ur import UR

# 创建机器人驱动
ur = UR()
# 连接机器人
ur.connect()
# 移动机器人
ur.move_j([-84.56,-87.06,-89.02,-96.33,90.87,89.87])  # J0下 - J5上

# ahkdfa TODO
#TODO
# prit("hello")