from sdk.ur import UR

# 创建驱动
ur = UR()

# 连接机械臂
ur.connect()

# 放松姿态
ur.move_j([-84.56, -87.06, -89.02, -96.33, 90.87, 89.87])

# 定义四个点
pos = [0.3, 0, 0, 180, 0, 90]

ur.clear_points()
ur.disable_trail()

ur.show_point((0, 0, 0), 0.1, [0, 255, 0, 0])  # 原点
ur.show_point((0.3, 0, 0))

# 移动到第一个点
ur.move_p(pos)
# 开启线路显示
ur.enable_trail()

# 修改坐标变成第二个点
pos[1] += 0.3
ur.move_p(pos)
# 修改坐标变成第三个点
pos[0] += 0.3
ur.move_p(pos)
# 修改坐标变成第四个点
pos[1] -= 0.3
ur.move_p(pos)
# 修改坐标变成第一个点
pos[0] -= 0.3
ur.move_p(pos)


pos_dynamic = pos
loop_count = 0
while loop_count < 5:


# count = 0
# while count < 5:
#     # 移动到第一个点
#     ur.move_p(pos)
#     # 开启线路显示
#     ur.enable_trail()
#
#     # 修改坐标变成第二个点
#     pos[1] += 0.1
#     ur.move_p(pos)
#     # 修改坐标变成第三个点
#     pos[0] += 0.3
#     ur.move_p(pos)
#     # 修改坐标变成第四个点
#     pos[1] -= 0.3
#     ur.move_p(pos)
#     # 修改坐标变成第一个点
#     pos[0] -= 0.3
#     ur.move_p(pos)
#
#     count += 1
