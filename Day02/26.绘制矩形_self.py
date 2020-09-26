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
# ur.move_p(pos)
# 开启线路显示
ur.enable_trail()

pos_1 = [0, 0, 0, 0, 0, 0]
pos_2 = [0, 0, 0, 0, 0, 0]
pos_3 = [0, 0, 0, 0, 0, 0]
pos_4 = [0, 0, 0, 0, 0, 0]

alpha = 0.5
delta = 0.01

# pos_1[0] -= delta
# pos_1[1] += delta
#
# pos_2[0] += delta
# pos_2[1] += delta
#
# print(pos_1)
# print(pos_2)
def increment_alpha():
    pos_1[0] -= alpha
    pos_1[1] += alpha

    pos_2[0] += alpha
    pos_2[1] += alpha

    pos_3[0] += alpha
    pos_3[1] -= alpha

    pos_4[0] -= alpha
    pos_4[1] -= alpha



def increment_delta():
    pos_1[0] -= delta
    pos_1[1] += delta

    pos_2[0] += delta
    pos_2[1] += delta

    pos_3[0] += delta
    pos_3[1] -= delta

    pos_4[0] -= delta
    pos_4[1] -= delta

    # print(pos_1)
    # print(pos_2)
    # print(pos_3)
    # print(pos_4)

loop_count = 0
increment_alpha()
while loop_count < 5:
    # pos_1[0] -= delta
    # pos_1[1] += delta
    #
    # pos_2[0] += delta
    # pos_2[1] += delta
    #
    # pos_3[0] += delta
    # pos_3[1] -= delta
    #
    # pos_4[0] -= delta
    # pos_4[1] -= delta

    increment_delta()

    print(pos_1)
    print(pos_2)
    print(pos_3)
    print(pos_4)

    # 移动到第一个点
    ur.move_p(pos_1)
    # 开启线路显示
    ur.enable_trail()

    ur.move_p(pos_2)
    ur.move_p(pos_3)
    ur.move_p(pos_4)


    loop_count += 1