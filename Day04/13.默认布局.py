from PyQt5.QtWidgets import QWidget, QApplication, QPushButton
# from PyQt5.QtGui import QIcon
import sys

# 创建PyQt程序(sys.argv 固定写法)
app = QApplication(sys.argv)
# 创建窗口
window = QWidget()
# 修改标题
window.setWindowTitle('默认布局')

# 创建按钮
btn1 = QPushButton('按钮1')
btn2 = QPushButton('按钮2')
# 显示按钮
btn1.setParent(window)
btn2.setParent(window)

# 展示窗口
window.show()
# 等待窗口停止,退出操作
sys.exit(app.exec())
