from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QLabel
from PyQt5.QtGui import QPainter,QPen,QColor
import sys

'''
自定义控件
1.定义控件类,继承QWidet
2.重写paintEvent方法,绘制效果
3.定义QPainter画家,开始绘画
'''


# 自定义控件
class MyWidget(QWidget):
    def __init__(self):
        super(MyWidget, self).__init__()
        # 设置控件大小
        self.setFixedSize(600,600)

    def mousePressEvent(self, event):
        '''
        鼠标按下事件 (每次按下鼠标会执行)
        :param event:
        :return:
        '''
        x = event.x()
        y = event.y()

        print('鼠标按下了',x,y)

    def mouseMoveEvent(self, event):
        '''
        鼠标移动
        :param event:
        :return:
        '''
        print('鼠标移动')

    def mouseReleaseEvent(self, event):
        '''
        鼠标松开(执行一次)
        :param event:
        :return:
        '''
        print('鼠标松开')

    def paintEvent(self, event):
        '''
        绘制方法
        :param event:事件
        :return:
        '''
        # 画家
        painter = QPainter(self)
        # 画笔
        pen = QPen()
        # 设置画笔颜色
        pen.setColor(QColor(0,0,255))
        # 替换画笔
        painter.setPen(pen)
        # 绘制文本
        painter.drawText(10,10,'hello')
        # 绘制直线
        # painter.drawLine(10,10,100,100)
        # 绘制圆弧
        # painter.drawArc(100,100,100,100,90*16,90*16)
        # painter.drawPolygon()



class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        # 设置标题
        self.setWindowTitle('自定义控件')
        # 创建控件
        widget = MyWidget()
        # 显示
        widget.setParent(self)


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
