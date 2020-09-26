from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QHBoxLayout
# from PyQt5.QtGui import QIcon
from widget.ArrowWidget import *
import sys

# 创建PyQt程序(sys.argv 固定写法)
app = QApplication(sys.argv)
# 创建窗口
window = QWidget()
# 修改标题
window.setWindowTitle('示教器第一部分')

# 创建整体布局
wholeLayout = QVBoxLayout()
# 添加整体布局
window.setLayout(wholeLayout)

# 创建第一部分和第二部分布局
layout1 = QHBoxLayout()
layout2 = QHBoxLayout()
# 放到整体的布局中
wholeLayout.addLayout(layout1)
wholeLayout.addLayout(layout2)

# 创建上部布局两个控件
zU = ArrowWidget('Z+', Direction.UP)
zD = ArrowWidget('Z-', Direction.DOWN)

# 放入第一个布局中
layout1.addWidget(zU)
layout1.addWidget(zD)

# 创建控件以及竖直的布局
yL = ArrowWidget('Y-', Direction.LEFT)
yR = ArrowWidget('Y+', Direction.RIGHT)
xU = ArrowWidget('X+', Direction.UP)
xD = ArrowWidget('X-', Direction.DOWN)

layout = QVBoxLayout()
layout.addWidget(xU)
layout.addWidget(xD)
# 添加第二部分布局
layout2.addWidget(yL)
layout2.addLayout(layout)
layout2.addWidget(yR)

# 展示窗口
window.show()
# 等待窗口停止,退出操作
sys.exit(app.exec())
