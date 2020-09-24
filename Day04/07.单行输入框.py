from PyQt5.QtWidgets import QWidget,QApplication,QLineEdit
from PyQt5.QtGui import QIcon
import sys

# 创建PyQt程序(sys.argv 固定写法)
app = QApplication(sys.argv)
# 创建窗口
window = QWidget()
# 修改标题
window.setWindowTitle('单行输入框')
# 创建单行输入框
edit = QLineEdit()
# 展示单行输入框
edit.setParent(window)
# 设置密码模式
edit.setEchoMode(QLineEdit.Password)
# 展示窗口
window.show()
# 等待窗口停止,退出操作
sys.exit(app.exec())