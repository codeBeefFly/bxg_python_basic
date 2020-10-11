from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtWidgets import QWidget

from locals import TYPE


class MyPaintWidget(QWidget):
    def __init__(self):
        super(MyPaintWidget, self).__init__()
        # 使用字典容器保存单个的点坐标，并将这些点坐标放入列表中
        self.points = []

    def clear(self):
        """
        清理画板，将列表存储的点清零，并更新 QWidget
        :return:
        """
        self.points.clear()  # 清空列表
        self.update()  # 更新QWidget对象

    def mousePressEvent(self, event):
        """
        方法重写
        鼠标按下事件处理
        :param event: 事件
        :return:
        """
        # 获取当前点的坐标
        x = event.x()
        y = event.y()
        # 将这些坐标放入点字典
        point = {'x': x, 'y': y, 'type': TYPE.PRESS}
        # 将点放入点列表
        self.points.append(point)
        # 记得更新QWidget
        # Calling update() several times normally results in just one paintEvent() call.
        self.update()

    def mouseMoveEvent(self, event):
        """
        方法重写
        鼠标按住移动事件处理
        :param event: 事件
        :return:
        """
        # 获取当前点的坐标
        x = event.x()
        y = event.y()
        # 将这些坐标放入点字典
        point = {'x': x, 'y': y, 'type': TYPE.MOVE}
        # 将点放入点列表
        self.points.append(point)
        # 记得更新QWidget
        # Calling update() several times normally results in just one paintEvent() call.
        self.update()

    def mouseReleaseEvent(self, event):
        """
        方法重写
        鼠标释放事件处理
        :param event: 事件
        :return:
        """
        # 获取当前点的坐标
        x = event.x()
        y = event.y()
        # 将这些坐标放入点字典
        point = {'x': x, 'y': y, 'type': TYPE.RELEASE}
        # 将点放入点列表
        self.points.append(point)
        # 记得更新QWidget
        # Calling update() several times normally results in just one paintEvent() call.
        self.update()

    def paintEvent(self, event):
        """
        绘制事件，创建画家，画笔，在MainWindow中没有用到
        :param event: 事件
        :return:
        """
        # 判断如果points为空，不需要绘制
        if len(self.points) == 0:
            return
        # 创建画家
        # QPainter::QPainter(QPaintDevice *device)
        # Constructs a painter that begins painting the paint device immediately.
        painter = QPainter(self)
        # 创建画笔
        pen = QPen()
        # 画家拿画笔
        painter.setPen(pen)
        # 设置起始点，为了形成闭环
        start_point = self.points[0]
        # 绘制路径，线段（start--end），从第二个点开始
        for index in range(1, len(self.points)):
            # 设置结束点
            end_point = self.points[index - 1]  # 因为index提前了一位
            # 绘制
            painter.drawLine(start_point['x'], start_point['y'], end_point['x'''], end_point['y'])
            # 需改起始点
            start_point = end_point
