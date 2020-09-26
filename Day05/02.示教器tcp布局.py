from PyQt5.QtWidgets import QWidget,QApplication,QVBoxLayout,QHBoxLayout,QLabel,QLineEdit
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from widget.ArrowWidget import *
import sys
# 1 竖直
# 2 水平
# 创建PyQt程序(sys.argv 固定写法)
app = QApplication(sys.argv)
# 创建窗口
window = QWidget()
# 修改标题
window.setWindowTitle('TCP布局')
# 定义整体的布局
wholeLayout = QVBoxLayout()
# 设置布局
window.setLayout(wholeLayout)
# 第一部分
xLayout = QHBoxLayout()
x = QLabel('X')
# 设置宽度
x.setFixedWidth(50)
# 设置x控件显示位置
x.setAlignment(Qt.AlignRight)
xEdit = QLineEdit()
# 设置不能输入
xEdit.setEnabled(False)
xUnit = QLabel('mm')
xUnit.setFixedWidth(50)
xLayout.addWidget(x)
xLayout.addWidget(xEdit)
xLayout.addWidget(xUnit)
wholeLayout.addLayout(xLayout)

# 第二部分
yLayout = QHBoxLayout()
y = QLabel('Y')
y.setFixedWidth(50)
# 设置x控件显示位置
y.setAlignment(Qt.AlignRight)
yEdit = QLineEdit()
yUnit = QLabel('mm')
yUnit.setFixedWidth(50)
yLayout.addWidget(y)
yLayout.addWidget(yEdit)
yLayout.addWidget(yUnit)
wholeLayout.addLayout(yLayout)

# 第三部分
zLayout = QHBoxLayout()
z = QLabel('Z')
z.setFixedWidth(50)
# 设置x控件显示位置
z.setAlignment(Qt.AlignRight)
zEdit = QLineEdit()
zUnit = QLabel('mm')
zUnit.setFixedWidth(50)
zLayout.addWidget(z)
zLayout.addWidget(zEdit)
zLayout.addWidget(zUnit)
wholeLayout.addLayout(zLayout)

# 第二部分
rxLayout = QHBoxLayout()
rx = QLabel('RX')
rx.setFixedWidth(50)
# 设置x控件显示位置
rx.setAlignment(Qt.AlignRight)
rxEdit = QLineEdit()
rxUnit = QLabel('rad')
rxUnit.setFixedWidth(50)
rxLayout.addWidget(rx)
rxLayout.addWidget(rxEdit)
rxLayout.addWidget(rxUnit)
wholeLayout.addLayout(rxLayout)

# # 第二部分
# yLayout = QHBoxLayout()
# y = QLabel('Y')
# yEdit = QLineEdit()
# yUnit = QLabel('mm')
# yLayout.addWidget(y)
# yLayout.addWidget(yEdit)
# yLayout.addWidget(yUnit)
# wholeLayout.addLayout(yLayout)
#
# # 第二部分
# yLayout = QHBoxLayout()
# y = QLabel('Y')
# yEdit = QLineEdit()
# yUnit = QLabel('mm')
# yLayout.addWidget(y)
# yLayout.addWidget(yEdit)
# yLayout.addWidget(yUnit)
# wholeLayout.addLayout(yLayout)

arrow = ArrowWidget('',Direction.RIGHT,TYPE.JOINTS)
wholeLayout.addWidget(arrow)

# 展示窗口
window.show()
# 等待窗口停止,退出操作
sys.exit(app.exec())