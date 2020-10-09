from PyQt5.QtGui import QPainter, QPen, QColor
from PyQt5.QtWidgets import QWidget, QApplication

import sys


class MyWidget(QWidget):
    def __init__(self):
        super(MyWidget, self).__init__()

    def paintEvent(self, event):
        """
        绘制方法
        :param event: 事件
        :return:
        """
        # 创建画家对象
        painter = QPainter(self)
        # 画笔
        pen = QPen()
        # 设置画笔颜色
        pen.setColor(QColor(100, 100, 255))
        # 画家拿起画笔
        painter.setPen(pen)
        # 画家绘制文本
        # void QPainter::drawText(int x, int y, const QString &text)
        # Draws the given text at position (x, y),
        # using the painter's currently defined text direction.
        painter.drawText(20, 20, 'hello')


class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        # 设置标题
        self.setWindowTitle('自定义控件')
        # 创建控件
        widget = MyWidget()
        # 将控件绑定在窗口
        widget.setParent(self)  # self就是MainWindow对象


def start():
    # 创建PyQt程序(sys.argv 固定写法)
    app = QApplication(sys.argv)
    # 创建窗口
    window = MainWindow()

    # 展示窗口
    window.show()
    # 等待窗口停止,退出操作
    sys.exit(app.exec())


if __name__ == '__main__':
    start()
