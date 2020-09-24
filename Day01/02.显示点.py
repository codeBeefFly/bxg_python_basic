from sdk.ur import UR

# 创建机器人驱动
ur = UR()
# 连接机器人
ur.connect()
# 显示点
ur.show_point((0.3, 0.4, 0))