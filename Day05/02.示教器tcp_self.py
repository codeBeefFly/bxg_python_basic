from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit
from widget.ArrowWidget import ArrowWidget
from widget.local import Direction, TYPE
import sys

####################################################
# 创建PyQt程序(sys.argv 固定写法)

app = QApplication(sys.argv)
# 创建窗口
window = QWidget()
# 修改标题
window.setWindowTitle('')
####################################################

# 定义整体布局
whole_layout = QVBoxLayout()
# 窗口设定成整体布局
window.setLayout(whole_layout)

# 定义字布局
sub_layout_1 = QHBoxLayout()
sub_layout_2 = QHBoxLayout()
sub_layout_3 = QHBoxLayout()
sub_layout_4 = QHBoxLayout()
sub_layout_5 = QHBoxLayout()
sub_layout_6 = QHBoxLayout()
# 添加到整体布局
whole_layout.addLayout(sub_layout_1)
whole_layout.addLayout(sub_layout_2)
whole_layout.addLayout(sub_layout_3)
whole_layout.addLayout(sub_layout_4)
whole_layout.addLayout(sub_layout_5)
whole_layout.addLayout(sub_layout_6)

# 子布局1添加组件
x_label = QLabel("X")
x_edit = QLineEdit()
x_unit = QLabel("mm")
sub_layout_1.addWidget(x_label)
sub_layout_1.addWidget(x_edit)
sub_layout_1.addWidget(x_unit)

# 子布局2添加组件
y_label = QLabel("Y")
y_edit = QLineEdit()
y_unit = QLabel("mm")
sub_layout_2.addWidget(y_label)
sub_layout_2.addWidget(y_edit)
sub_layout_2.addWidget(y_unit)

# 子布局3添加组件
z_label = QLabel("Z")
z_edit = QLineEdit()
z_unit = QLabel("mm")
sub_layout_3.addWidget(z_label)
sub_layout_3.addWidget(z_edit)
sub_layout_3.addWidget(z_unit)

# 子布局4添加组件
rx_label = QLabel("RX")
rx_edit = QLineEdit()
rx_unit = QLabel("rad")
sub_layout_4.addWidget(rx_label)
sub_layout_4.addWidget(rx_edit)
sub_layout_4.addWidget(rx_unit)

# 子布局5添加组件
ry_label = QLabel("RY")
ry_edit = QLineEdit()
ry_unit = QLabel("rad")
sub_layout_5.addWidget(ry_label)
sub_layout_5.addWidget(ry_edit)
sub_layout_5.addWidget(ry_unit)

# 子布局6添加组件
rz_label = QLabel("RZ")
rz_edit = QLineEdit()
rz_unit = QLabel("rad")
sub_layout_6.addWidget(rz_label)
sub_layout_6.addWidget(rz_edit)
sub_layout_6.addWidget(rz_unit)

# 设置label宽度
x_label.setFixedWidth(50)
y_label.setFixedWidth(50)
z_label.setFixedWidth(50)
rx_label.setFixedWidth(50)
ry_label.setFixedWidth(50)
rz_label.setFixedWidth(50)

# 设置label对齐
x_label.setAlignment(Qt.AlignRight)
y_label.setAlignment(Qt.AlignRight)
z_label.setAlignment(Qt.AlignRight)
rx_label.setAlignment(Qt.AlignRight)
ry_label.setAlignment(Qt.AlignRight)
rz_label.setAlignment(Qt.AlignRight)

x_unit.setFixedWidth(50)
y_unit.setFixedWidth(50)
z_unit.setFixedWidth(50)
rx_unit.setFixedWidth(50)
ry_unit.setFixedWidth(50)
rz_unit.setFixedWidth(50)

# 设置 editor 属性
x_edit.setEnabled(False)

# 增加小箭头图标
arrow = ArrowWidget("", Direction.RIGHT, TYPE.JOINTS)
whole_layout.addWidget(arrow)

####################################################
# 设置大小
# window.resize(800, 800)
# 展示窗口
window.show()
# 等待窗口停止,退出操作
sys.exit(app.exec())
####################################################