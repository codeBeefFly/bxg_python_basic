from PyQt5.QtWidgets import QWidget,QApplication,QGridLayout,QPushButton
from PyQt5.QtGui import QIcon
import sys

def func():
    # 打印不同的按钮文字
    # 获取信号发送者
    msg = window.sender().text()
    print('点击了按钮',msg)

# 创建PyQt程序(sys.argv 固定写法)
app = QApplication(sys.argv)
# 创建窗口
window = QWidget()
# 修改标题
window.setWindowTitle('网格布局')
# 创建整体布局
wholeLayout = QGridLayout()
# 设置布局
window.setLayout(wholeLayout)
# 控件
btn1 = QPushButton('A')
btn2 = QPushButton('B')
btn3 = QPushButton('C')
btn4 = QPushButton('D')
btn5 = QPushButton('E')
btn6 = QPushButton('F')
# 添加控件到布局中
# 参数1:控件 参数2:行  参数3:列
wholeLayout.addWidget(btn1,0,0)  # 0行，0列
wholeLayout.addWidget(btn2,0,1)  # 0行，1列
wholeLayout.addWidget(btn3,0,2)
wholeLayout.addWidget(btn4,1,0)
wholeLayout.addWidget(btn5,1,1)
wholeLayout.addWidget(btn6,1,2)

# 6个按钮信号和槽绑定
btn1.clicked.connect(func)
btn2.clicked.connect(func)
btn3.clicked.connect(func)
btn4.clicked.connect(func)
btn5.clicked.connect(func)
btn6.clicked.connect(func)

# 展示窗口
window.show()
# 等待窗口停止,退出操作
sys.exit(app.exec())