from enum import Enum

# 方向
class Direction(Enum):
    LEFT = 0
    RIGHT = 1
    UP = 2
    DOWN = 3

# 类型:
class TYPE(Enum):
    TCP = 0 # 普通调节坐标和姿态
    JOINTS = 1 # 关节角

