from enum import Enum


class TYPE(Enum):
    PRESS = 0  # 点的类型，按下
    MOVE = 1  # 点的类型，移动
    RELEASE = 2  # 点的类型，松开
