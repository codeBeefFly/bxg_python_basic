from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPainter,QPen,QColor
from locals import *
'''
绘制自定义控件
paintEvent只会在界面第一次显示的时候主动调用,后面不再主动调用
'''


class PaintWidget(QWidget):
    def __init__(self):
        super(PaintWidget, self).__init__()
        # 容器,保存鼠标经过的所有的点
        # 点数据类型:字典  {'x':x,'y':y,'type:type}
        self.points = []

    def clear(self):
        '''
        清理画板
        :return:
        '''
        # 清空点的列表
        self.points.clear()
        # 重新绘制
        self.update()


    def mousePressEvent(self, event):
        '''
        鼠标按下
        :param event:
        :return:
        '''
        x = event.x()
        y = event.y()
        # 创建点
        point = {'x':x,'y':y,'type':TYPE.DOWN}
        # 添加到容器中
        self.points.append(point)
        # 主动绘制
        # update 自动调用paintEvent
        self.update()

    def mouseMoveEvent(self, event):
        '''
        鼠标移动
        :param event:
        :return:
        '''
        x = event.x()
        y = event.y()
        # 创建点
        point = {'x': x, 'y': y, 'type': TYPE.MOVE}
        # 添加到容器中
        self.points.append(point)
        # 主动绘制
        self.update()

    def mouseReleaseEvent(self, event):
        '''
        鼠标松开
        :param event:
        :return:
        '''
        x = event.x()
        y = event.y()
        # 创建点
        point = {'x': x, 'y': y, 'type': TYPE.UP}
        # 添加到容器中
        self.points.append(point)
        # 主动绘制
        self.update()

    def paintEvent(self, event):
        '''
        绘制事件
        :param event:
        :return:
        '''
        # 如果点的列表为空,不需要绘制
        if len(self.points)==0:
            return

        # 创建画家
        painter = QPainter(self)
        # 创建画笔
        pen = QPen()
        # 设置画笔颜色
        pen.setColor(QColor(255,0,0))
        # 设置画笔
        painter.setPen(pen)
        # 绘制已经走过的点  10个点,如何绘制
        startPoint = self.points[0]
        for index in range(1,len(self.points)):
            # 获取结束的点
            endPoint = self.points[index]
            # 绘制
            painter.drawLine(startPoint['x'],startPoint['y'],endPoint['x'],endPoint['y'])
            # 修改起点
            startPoint = endPoint


