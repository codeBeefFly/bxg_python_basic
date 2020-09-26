from PyQt5.QtWidgets import QWidget, QPushButton
from PyQt5.QtGui import QPen, QPainter, QColor, QPolygon, QBrush
from PyQt5.QtCore import Qt, QPoint
from widget.local import Direction, TYPE
# from local import Direction, TYPE


class ArrowWidget(QWidget):
    def __init__(self, text, direction, type=TYPE.TCP):
        super(ArrowWidget, self).__init__()
        # 类型
        self.type = type
        # 文字
        self.text = text
        if type == TYPE.JOINTS:
            self.setFixedSize(20, 20)
            if direction == Direction.LEFT:
                self.poitns = [QPoint(0, 10), QPoint(10, 20), QPoint(10, 15), QPoint(20, 15), QPoint(20, 5),
                               QPoint(10, 5), QPoint(10, 0), QPoint(0, 10)]
            elif direction == Direction.RIGHT:
                self.poitns = [QPoint(20, 10), QPoint(10, 0), QPoint(10, 5), QPoint(0, 5), QPoint(0, 15),
                               QPoint(10, 15), QPoint(10, 20), QPoint(20, 10)]
            self.color = '#80CAFE'
            return

        # 设置控件大小
        self.setFixedSize(60, 60)
        if direction == Direction.UP:
            self.poitns = [QPoint(30, 0), QPoint(0, 30), QPoint(15, 30), QPoint(15, 60), QPoint(45, 60), QPoint(45, 30),
                           QPoint(60, 30), QPoint(30, 0)]
            self.pos = (25, 25)
        elif direction == Direction.DOWN:
            self.poitns = [QPoint(30, 60), QPoint(60, 30), QPoint(45, 30), QPoint(45, 0), QPoint(15, 0), QPoint(15, 30),
                           QPoint(0, 30), QPoint(30, 60)]
            self.pos = (25, 40)
        elif direction == Direction.LEFT:
            self.poitns = [QPoint(0, 30), QPoint(30, 60), QPoint(30, 45), QPoint(60, 45), QPoint(60, 15),
                           QPoint(30, 15), QPoint(30, 0), QPoint(0, 30)]
            self.pos = (15, 35)
        elif direction == Direction.RIGHT:
            self.poitns = [QPoint(60, 30), QPoint(30, 0), QPoint(30, 15), QPoint(0, 15), QPoint(0, 45), QPoint(30, 45),
                           QPoint(30, 60), QPoint(60, 30)]
            self.pos = (35, 35)
        # 颜色
        if self.text.find('X') != -1:
            self.color = '#FF9FA1'
        elif self.text.find('Y') != -1:
            self.color = '#7EDF81'
        elif self.text.find('Z') != -1:
            self.color = '#80CAFE'

    def mousePressEvent(self, event):
        self.originalColor = self.color
        self.color = '#888783'
        self.update()

    def mouseReleaseEvent(self, QMouseEvent):
        self.color = self.originalColor
        self.update()

    def paintEvent(self, event):
        # 画家
        painter = QPainter(self)
        # 画笔
        pen = QPen(QColor(self.color))
        # 设置画笔和画刷
        painter.setPen(pen)
        painter.setBrush(QBrush(QColor(self.color)))
        # 绘制轮廓
        painter.drawPolygon(QPolygon(self.poitns), len(self.poitns))
        # 绘制
        # 画笔
        pen = QPen(QColor('#000000'))
        # 设置画笔和画刷
        painter.setPen(pen)
        if self.type == TYPE.TCP:
            painter.drawText(*self.pos, self.text)
