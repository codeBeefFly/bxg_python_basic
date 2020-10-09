from PyQt5.QtGui import QPainter, QPen, QColor
from PyQt5.QtWidgets import QWidget, QApplication

import sys


class MyWidget(QWidget):
    # 在不重写父类 init 方法时，在子类不写 init
    # def __init__(self):
    #     super(MyWidget, self).__init__()

    mouse_count = 0  # 静态变量

    def __init__(self):
        super(MyWidget, self).__init__()
        # 设置控件大小
        self.setFixedSize(600, 600)

    def get_mouse_count(self):
        return MyWidget.mouse_count

    def zero_mouse_count(self):
        MyWidget.mouse_count = 0
        return  MyWidget.mouse_count

    def increase_mouse_count(self, increment):
        return MyWidget.mouse_count + increment

    def paintEvent(self, event):
        # 创建画家对象
        painter = QPainter()
        # 创建画笔
        pen = QPen()
        # 设置画笔颜色
        pen.setColor(QColor(100, 100, 255))
        # 画家拿起画笔
        painter.setPen(pen)
        # 画家绘制文本
        painter.drawText(20, 20, 'hello world')

    def mouseReleaseEvent(self, event):
        # mouse_count = 0
        print('鼠标释放')

    def mouseMoveEvent(self, event):
        # mouse_count_inner = self.increase_mouse_count(1)
        # print('len of event::', len(event))
        print('event[{}]'.format(event))
        x = event.x()
        y = event.y()
        # mouse_count_inner = event.x() / event.x() + 1
        # print('鼠标移动，坐标({}, {})，次数({})'.format(x, y, mouse_count_inner))
        print('鼠标移动，坐标({}, {})'.format(x, y))  # 思考，如何输出次数

    def mousePressEvent(self, event):
        mouse_count_inner = self.zero_mouse_count()
        x = event.x()
        y = event.y()
        print('鼠标按下，坐标({}, {})，次数({})'.format(x, y, mouse_count_inner))


class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        # 创建控件
        widget = MyWidget()
        # 将控件绑定在MainWindow 对象
        widget.setParent(self)


def start():
    # 创建PyQt程序(sys.argv 固定写法)
    app = QApplication(sys.argv)
    # 创建窗口
    window = MainWindow()
    # 修改标题
    window.setWindowTitle('自定义鼠标事件')
    # 设置大小
    window.resize(800, 800)
    # 展示窗口
    window.show()
    # 等待窗口停止,退出操作
    sys.exit(app.exec())


if __name__ == '__main__':
    start()
