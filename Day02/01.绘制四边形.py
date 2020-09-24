from sdk.ur import UR

# 创建驱动
ur = UR()

# 连接机械臂
ur.connect()

# 放松姿态
ur.move_j([-84.56,-87.06,-89.02,-96.33,90.87,89.87])

# 清除点
ur.clear_points()

# 定义四个点
pos1 = [0.3,0,0,180,0,90]
pos2 = [0.3,0.3,0,180,0,90]
pos3 = [0.6,0.3,0,180,0,90]
pos4 = [0.6,0,0,180,0,90]

# 显示点
ur.show_point((0.6,0.3,0))
ur.show_point((0.3,0.3,0))
ur.show_point((0.3,0,0))
ur.show_point((0.6,0,0))

# 绘制
while True:
    ur.move_l(pos1)
    # 显示路线

    ur.enable_trail()
    # ur.move_p(pos2)
    # ur.move_p(pos3)
    # ur.move_p(pos4)
    # ur.move_p(pos1)

    ur.move_l(pos2)
    ur.move_l(pos3)
    ur.move_l(pos4)
    ur.move_l(pos1)