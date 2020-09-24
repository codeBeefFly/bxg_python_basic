from PyQt5.QtWidgets import QWidget,QApplication,QLabel
from PyQt5.QtGui import QIcon,QFont
import sys

# 创建PyQt程序(sys.argv 固定写法)
app = QApplication(sys.argv)
# 创建窗口
window = QWidget()
# 修改标题
window.setWindowTitle('文本')
# 创建文本
label = QLabel('黑马程序员机器人学科')
# 设置字体和大小
font = QFont('宋体',50)
# 设置字体和大小
label.setFont(font)
# label显示在窗口上
label.setParent(window)
# 展示窗口
window.show()
# 等待窗口停止,退出操作
sys.exit(app.exec())