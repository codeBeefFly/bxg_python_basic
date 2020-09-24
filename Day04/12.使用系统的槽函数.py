from PyQt5.QtWidgets import QWidget,QApplication,QPushButton
from PyQt5.QtGui import QIcon
import sys

# 槽函数就是普通函数
def func():
    # 退出窗口
    QApplication.quit()

# 创建PyQt程序(sys.argv 固定写法)
app = QApplication(sys.argv)
# 创建窗口
window = QWidget()
# 修改标题
window.setWindowTitle('信号和槽')

# 创建按钮
btn = QPushButton('点我')
# 显示按钮
btn.setParent(window)

# 连接信号和槽
# 注意:
# 信号不需要()
# 槽函数也不需要()
btn.clicked.connect(QApplication.quit)

# 展示窗口
window.show()
# 等待窗口停止,退出操作
sys.exit(app.exec())