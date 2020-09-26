from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QHBoxLayout
from widget.ArrowWidget import ArrowWidget
from widget.local import Direction, TYPE
import sys

####################################################
# 创建PyQt程序(sys.argv 固定写法)
app = QApplication(sys.argv)
# 创建窗口
window = QWidget()
# 修改标题
window.setWindowTitle('示教器[jacob_v1]')
####################################################

# 创建整体布局
whole_layout = QVBoxLayout()
# 设置窗口布局方式
window.setLayout(whole_layout)

# 定义整个布局中四个子部分布局
sub_layout_1 = QHBoxLayout()
sub_layout_2 = QHBoxLayout()
sub_layout_3 = QHBoxLayout()
sub_layout_4 = QHBoxLayout()
# 将子布局添加到整体布局
whole_layout.addLayout(sub_layout_1)
whole_layout.addLayout(sub_layout_2)
whole_layout.addLayout(sub_layout_3)
whole_layout.addLayout(sub_layout_4)

# 定义子布局2，4中间布局为垂直布局
sub_layout_2_mid = QVBoxLayout()
sub_layout_4_mid = QVBoxLayout()

# sub_layout_1添加组件
zU = ArrowWidget("Z+", Direction.UP)
zD = ArrowWidget("Z-", Direction.DOWN)
sub_layout_1.addWidget(zU)
sub_layout_1.addWidget(zD)

# sub_layout_2添加组件+mid布局
yL = ArrowWidget("Y-", Direction.LEFT)
yR = ArrowWidget("Y+", Direction.RIGHT)
xU = ArrowWidget("X+", Direction.UP)
xD = ArrowWidget("X-", Direction.DOWN)
sub_layout_2_mid.addWidget(xU)
sub_layout_2_mid.addWidget(xD)
sub_layout_2.addWidget(yL)
sub_layout_2.addLayout(sub_layout_2_mid)
sub_layout_2.addWidget(yR)

# sub_layout_3添加组件
rzL = ArrowWidget("RZ+", Direction.LEFT)
rzR = ArrowWidget("RZ-", Direction.RIGHT)
sub_layout_3.addWidget(rzL)
sub_layout_3.addWidget(rzR)

# sub_layot_4添加组件+mid布局
ryL = ArrowWidget("RY-", Direction.LEFT)
ryR = ArrowWidget("RY+", Direction.RIGHT)
rxU = ArrowWidget("RX+", Direction.UP)
rxD = ArrowWidget("RX-", Direction.DOWN)
sub_layout_4_mid.addWidget(rxU)
sub_layout_4_mid.addWidget(rxD)
sub_layout_4.addWidget(ryL)
sub_layout_4.addLayout(sub_layout_4_mid)
sub_layout_4.addWidget(ryR)


####################################################
# 设置大小
# window.resize(800, 800)
# 展示窗口
window.show()
# 等待窗口停止,退出操作
sys.exit(app.exec())
####################################################