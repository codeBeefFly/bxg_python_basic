from PyQt5.QtWidgets import QWidget, QApplication

import sys

####################################################
# 创建PyQt程序(sys.argv 固定写法)
app = QApplication(sys.argv)
# 创建窗口
window = QWidget()
# 修改标题
window.setWindowTitle('pyqt面向过程')
####################################################



####################################################
# 设置大小
window.resize(800, 800)
# 展示窗口
window.show()
# 等待窗口停止,退出操作
sys.exit(app.exec())
####################################################