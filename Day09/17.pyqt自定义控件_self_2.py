from PyQt5.QtWidgets import QWidget, QApplication

import sys


class MainWindow(QWidget):
    def __init__(self):
        # 调用父类初始化方法
        super(MainWindow, self).__init__()
        # 设置窗口标题
        # self.setWindowTitle('自定义控件2')
        # 设置窗口大小
        # self.resize(640, 480)
        # 展示窗口
        # self.show()


def start():
    # 创建PyQt程序(sys.argv 固定写法)
    app = QApplication(sys.argv)
    # 创建窗口
    window = MainWindow()


    # 设置窗口标题
    # window.setWindowTitle('类外，自定义控件2')  # 类外定义可以覆盖类中定义
    # 设置大小
    # window.resize(900, 900)  # 类外定义可以覆盖类中定义


    # 展示窗口
    window.show()
    # 等待窗口停止,退出操作
    sys.exit(app.exec())


if __name__ == '__main__':
    start()