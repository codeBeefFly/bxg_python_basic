from PyQt5.QtWidgets import QWidget,QApplication,QVBoxLayout,QPushButton
from PyQt5.QtGui import QIcon
from  MainWindow import MainWindow
import sys

#
# class MyWidget(QWidget):
#     def button_widget(self):
#         pass

'''---------------------- 窗口类 ----------------------'''
class MainWindow(QWidget):
    def __init__(self):
        # 父类 init中会执行一些初始化
        # 调用父类的init方法
        super(MainWindow, self).__init__()
        # 创建布局
        layout = QVBoxLayout()
        # 设置窗口布局
        self.setLayout(layout)
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


def start():
    # 创建PyQt程序(sys.argv 固定写法)
    app = QApplication(sys.argv)
    # 创建窗口
    window = MainWindow()

    # 展示窗口
    window.show()
    # 等待窗口停止,退出操作
    sys.exit(app.exec())


def start_2():
    # 创建PyQt程序(sys.argv 固定写法)
    app = QApplication(sys.argv)
    # 创建窗口
    window = QWidget()

    # 创建布局
    # 就是把layout放进类中，这个类就是继承自QWidget的窗口类
    layout = QVBoxLayout()
    # 设置窗口布局
    window.setLayout(layout)
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

    # 展示窗口
    window.show()
    # 等待窗口停止,退出操作
    sys.exit(app.exec())


if __name__ == '__main__':
    start()
    # start_2()