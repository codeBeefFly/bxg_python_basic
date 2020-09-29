from PyQt5.QtWidgets import QWidget,QApplication,QVBoxLayout,QPushButton

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