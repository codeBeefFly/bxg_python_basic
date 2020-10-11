from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton

from MyPaintWidget import MyPaintWidget
from sdk.ur import UR


class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ur = None
        # self.whole_layout = None
        self.clear_button = None
        self.paint_button = None
        self.paint_widget = None
        self._init_sdk()
        self._init_window()
        self._init_widget()  # widget 在 layout 前面
        self._init_layout()

    def _init_sdk(self):
        self.ur = UR()
        self.ur.connect()

    def _init_window(self):
        self.setWindowTitle('robot paint self')
        self.setFixedSize(640, 480)

    def _init_layout(self):
        whole_layout = QVBoxLayout()
        top_layout = QHBoxLayout()
        self.setLayout(whole_layout)
        whole_layout.addLayout(top_layout)
        whole_layout.addWidget(self.paint_widget)
        top_layout.addWidget(self.clear_button)
        top_layout.addWidget(self.paint_button)

    def _init_widget(self):
        self.paint_widget = MyPaintWidget()
        self.clear_button = QPushButton('清理')
        self.paint_button = QPushButton('绘制')
        self.clear_button.clicked.connect(self.clear)
        self.paint_button.clicked.connect(self.paint)

    def clear(self):
        self.paint_widget.clear()

    def scale_data(self, x, y):
        """
        画板坐标映射到机器人坐标
        :param x: 画板 x 坐标
        :param y: 画板 y 坐标
        :return: 机器人 x，y 坐标
        """
        x = 0.3 - 0.6 * x / 640
        y = -0.5 + 0.4 * y / 480
        return x, y

    def paint(self):
        """
        调用机器人sdk
        :return:
        """
        # 使用move_j移动至放松位置
        self.ur.move_j([-84.56, -87.06, -89.02, -96.33, 90.87, 89.87])
        # PaintWidget(自定义)对象paint_widget 获取所有绘画点
        points = self.paint_widget.points[::10]  # 每隔十个点选取
        # 开启sdk轨迹
        self.ur.enable_trail()
        # 绘制这些点
        for point in points:  # points 字典吗？
            px = point['x']
            py = point['y']
            # 使用move_p 方式移动可以提高效率的同时精确画图
            x, y = self.scale_data(px, py)
            self.ur.move_p([x, y, 0.45422, 180, 0, 90])
