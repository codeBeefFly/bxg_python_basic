from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QPushButton

import sys


class MyWindow(QWidget):
    def __init__(self):
        # 调用父类init
        super(MyWindow, self).__init__()
        # 创建布局
        self._init_layout()

    def _init_layout(self):
        # 创建布局
        layout = QVBoxLayout()
        # 设置窗口布局
        self.setLayout(layout)  # MyWindow就是QWidget对象，相当于window.setLayout(layout)
        # 创建5个按钮
        btn1 = QPushButton('1')
        btn2 = QPushButton('2')
        btn3 = QPushButton('3')
        btn4 = QPushButton('4')
        btn5 = QPushButton('5')
        # 添加到布局中
        layout.addWidget(btn1)
        layout.addWidget(btn2)
        layout.addWidget(btn3)
        layout.addWidget(btn4)
        layout.addWidget(btn5)


####################################################
# 创建PyQt程序(sys.argv 固定写法)
app = QApplication(sys.argv)
# # 创建窗口，从这里开始使用类对象
# window = QWidget()
window = MyWindow()
# # 修改标题
window.setWindowTitle('pyqt面向对象')
####################################################



####################################################
# 设置大小
window.resize(800, 800)
# 展示窗口
window.show()
# 等待窗口停止,退出操作
sys.exit(app.exec())
####################################################