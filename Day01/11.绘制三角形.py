'''
需求:
定义三个点变量,移动机器人绘制三角形
'''
from sdk.ur import UR
# 定义三个点
# 姿态位姿, x, y, z, rx, ry, rz, xyz单位是米，rx,ry,rz 单位是角度
pos1 = [0.3,0,0,180,0,90]  # x, y, z, rx, ry, rz, 末端位姿的 xyz与旋转角度
pos2 = [0,0.3,0,180,0,90]  # x, y, z, rx, ry, rz
pos3 = [0.3,0.3,0,180,0,90]  # x, y, z, rx, ry, rz

# 创建驱动
ur = UR()
# 显示三个点
ur.show_point((0.3,0,0))
ur.show_point((0,0.3,0))
ur.show_point((0.3,0.3,0))
# 连接机械臂
ur.connect()
# 把机械臂关节放松
ur.move_j([-84.56,-87.06,-89.02,-96.33,90.87,89.87])
# 移动到第一个点
ur.move_l(pos1)
# 显示路线
ur.enable_trail()
# 移动到第二个点
ur.move_l(pos2)
# 移动到第三个点
ur.move_l(pos3)
# 移动到第一个点
ur.move_l(pos1)

