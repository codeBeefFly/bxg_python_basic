'''
需求:
定义三个点变量,移动机器人绘制三角形
'''
from sdk.ur import UR
# 定义三个点
# 关节角度 J0, ..., J5, 单位是角度
pos1 = [21.34,-114.95,-154.25,-0.81,89.97,201.39]  #
pos2 = [111.33,-114.97,-154.26,-0.72,90.01,291.31]
pos3 = [59.91,-119.35,-134.83,-15.77,90.01,239.88]

# 创建驱动
ur = UR()

ur.clear_points()
ur.disable_trail()

# 显示三个点
ur.show_point((0.3,0,0))
ur.show_point((0,0.3,0))
ur.show_point((0.3,0.3,0))

# 连接机械臂
ur.connect()

# 把机械臂关节放松
ur.move_j([-84.56,-87.06,-89.02,-96.33,90.87,89.87])

# 移动到第一个点
ur.move_j(pos1)
# 显示路线
ur.enable_trail()
# 移动到第二个点
ur.move_j(pos2)
# 移动到第三个点
ur.move_j(pos3)
# 移动到第一个点
ur.move_j(pos1)

