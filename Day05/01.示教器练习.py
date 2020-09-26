# from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QHBoxLayout
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QHBoxLayout
from PyQt5.QtGui import QIcon
from widget.ArrowWidget import *
import sys

# 创建PyQt程序(sys.argv 固定写法)
app = QApplication(sys.argv)
# 创建窗口
window = QWidget()
# 修改标题
window.setWindowTitle('示教器')

# 整体布局
wholeLayout = QVBoxLayout()
# 设置窗口布局方式
window.setLayout(wholeLayout)

# 四部分布局定义
layout1 = QHBoxLayout()
layout2 = QHBoxLayout()
layout3 = QHBoxLayout()
layout4 = QHBoxLayout()

# 添加四部分布局到整体的布局中
wholeLayout.addLayout(layout1)
wholeLayout.addLayout(layout2)
wholeLayout.addLayout(layout3)
wholeLayout.addLayout(layout4)

# 第二部分竖直布局
layout2_2 = QVBoxLayout()
# 第四部分竖直布局
layout4_2 = QVBoxLayout()

# 第一部分布局控件
zU = ArrowWidget('Z+', Direction.UP)
zD = ArrowWidget('Z-', Direction.DOWN)
layout1.addWidget(zU)
layout1.addWidget(zD)

# 第二部分布局控件
yL = ArrowWidget('Y-', Direction.LEFT)
yR = ArrowWidget('Y+', Direction.RIGHT)
xU = ArrowWidget('X+', Direction.UP)
xD = ArrowWidget('X-', Direction.DOWN)
layout2.addWidget(yL)
layout2_2.addWidget(xU)
layout2_2.addWidget(xD)
layout2.addLayout(layout2_2)
layout2.addWidget(yR)

# 第三部分布局控件
rzL = ArrowWidget('RZ+', Direction.LEFT)
rzR = ArrowWidget('RZ-', Direction.RIGHT)
layout3.addWidget(rzL)
layout3.addWidget(rzR)

# 第四部分布局控件
ryL = ArrowWidget('RY-', Direction.LEFT)
ryR = ArrowWidget('RY+', Direction.RIGHT)
rxU = ArrowWidget('RX+', Direction.UP)
rxD = ArrowWidget('RX-', Direction.DOWN)
layout4.addWidget(ryL)
layout4_2.addWidget(rxU)
layout4_2.addWidget(rxD)
layout4.addLayout(layout4_2)
layout4.addWidget(ryR)

# 展示窗口
window.show()
# 等待窗口停止,退出操作
sys.exit(app.exec())
