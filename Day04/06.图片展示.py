from PyQt5.QtWidgets import QWidget,QApplication,QLabel
from PyQt5.QtGui import QIcon,QPixmap
import sys

# 创建PyQt程序(sys.argv 固定写法)
app = QApplication(sys.argv)
# 创建窗口
window = QWidget()
# 修改标题
window.setWindowTitle('图片展示')

# 创建Qlabel
label = QLabel()
# 创建图片的QPixmap
pixMap = QPixmap('i.jpg')
# 设置图片
label.setPixmap(pixMap)
# 控件展示到窗口上
label.setParent(window)

# 展示窗口
window.show()
# 等待窗口停止,退出操作
sys.exit(app.exec())