from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton
from PaintWidget import PaintWidget
from sdk.ur import UR


class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        # 机器人驱动
        self.ur = UR()
        # 连接
        self.ur.connect()
        # 设置标题
        self.setWindowTitle('机器人绘制')
        # 设置窗口大小
        self.setFixedSize(640, 480)
        # 创建整体布局
        wholeLayout = QVBoxLayout()
        # 设置布局
        self.setLayout(wholeLayout)
        # 创建上部布局
        topLayout = QHBoxLayout()
        # 添加布局到整体布局中
        wholeLayout.addLayout(topLayout)
        # 创建两个按钮
        clearBtn = QPushButton('清理')
        paintBtn = QPushButton('绘制')
        # 按钮添加到布局中
        topLayout.addWidget(clearBtn)
        topLayout.addWidget(paintBtn)
        # 创建自定义控件
        self.paintWidget = PaintWidget()
        # 添加到整体布局中
        wholeLayout.addWidget(self.paintWidget)
        # 设置按钮点击事件
        # 槽函数可以是普通函数 也可以是类的方法
        clearBtn.clicked.connect(self.clear)
        # 绘制事件
        paintBtn.clicked.connect(self.paint)

    def clear(self):
        '''
        清理
        :return:
        '''
        self.paintWidget.clear()

    def scaleData(self, x, y):
        '''
        对数据缩放处理
        :param cal:
        :return:
        '''
        x = 0.3 - 0.6 * x / 640
        y = -0.5 + 0.4 * y / 480
        return x, y

    def paint(self):
        '''
        调用机器人绘制
        :return:
        '''
        self.ur.disable_trail()
        self.ur.move_j([-84.56, -87.06, -89.02, -96.33, 90.87, 89.87])
        # 获取所有的点
        points = self.paintWidget.points[::10]
        self.ur.enable_trail()
        # 绘制点的数量
        # 遍历所有的点,移动过去
        for point in points:
            px = point['x']
            py = point['y']
            # print(px, py)
            # 移动 采用哪一种移动方式? movel movep
            # pose:[x,y,z,rx,ry,rz]
            # 缩放x和y
            x, y = self.scaleData(px, py)
            # print(x, y)
            print("(px, py)::({}, {}), (x, y)::({}, {})".format(px, py, x, y))
            # x y z 单位:m
            self.ur.move_p([x, y, 0.45422, 180, 0, 90])
