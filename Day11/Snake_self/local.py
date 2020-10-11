from enum import Enum
# 屏幕宽度
WINDOWWIDTH = 640
# 屏幕高度
WINDOWHEIGHT = 480

# 小方格的大小
CELLSIZE = 20

# 横向和纵向的方格数
CELLWIDTH = int(WINDOWWIDTH / CELLSIZE)
CELLHEIGHT = int(WINDOWHEIGHT / CELLSIZE)

# 定义常用颜色
WHITE = (255, 255, 255)
BLACK = ( 0, 0, 0)
RED = (255, 0, 0)
GREEN = ( 0, 255, 0)
DARKGREEN = ( 0, 155, 0)
DARKGRAY = ( 40, 40, 40)
BGCOLOR = BLACK

class Direction(Enum):
    LEFT = 0
    RIGHT = 1
    UP = 2
    DOWN = 3