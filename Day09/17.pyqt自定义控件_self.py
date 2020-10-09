from PyQt5.QtWidgets import QWidget, QApplication

import sys


class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        # 设置标题
        self.setWindowTitle('自定义控件')
        # 设置窗口大小
        self.resize(640, 480)
        # 展示窗口
        self.show()

####################################################
# 创建PyQt程序(sys.argv 固定写法)
app = QApplication(sys.argv)
# 创建窗口
window = MainWindow()
####################################################



####################################################
# 等待窗口停止,退出操作
sys.exit(app.exec())
####################################################