from MainWindow import MainWindow
from PyQt5.QtWidgets import QApplication
import sys


def start():
    '''
    开始
    :return:
    '''
    # 创建程序
    app = QApplication(sys.argv)
    # 创建窗口
    window = MainWindow()
    # 显示窗口
    window.show()
    # 等待窗口关闭
    sys.exit(app.exec())


if __name__ == '__main__':
    start()
