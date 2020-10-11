import sys

from PyQt5.QtWidgets import QApplication

from MainWindow import MainWindow


def start():
    # 创建一个 application 对象
    # 创建一个 window 对象
    # window 对象调用 show
    # 退出
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()  # MainWindow 还没有定义，所以 unresolved
    sys.exit(app.exec())  # exec 调用 exit 返回 0 或 非0


if __name__ == '__main__':
    start()
