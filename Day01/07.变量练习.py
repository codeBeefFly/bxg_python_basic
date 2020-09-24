'''
定义一个点的变量,移动机械臂到这个点
'''
from sdk.ur import UR
# 6个关节角
joints = [-84.56,-87.06,-89.02,-96.33,90.87,89.87]

# 创建驱动
ur = UR()
# 连接机械臂
ur.connect()
# 移动机械臂达到对应的位置
ur.move_j(joints)
