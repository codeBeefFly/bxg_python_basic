""" 计算器 self
目的：快速的学习pyqt编程结构
方法：理解代码思维，实现功能，可以直接复制粘贴课程代码
"""
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QApplication, QGridLayout, QLabel, QPushButton  # for create a window
import sys

####################################################
# 创建PyQt程序(sys.argv 固定写法)
app = QApplication(sys.argv)
# 创建窗口
window = QWidget()
# 修改标题
window.setWindowTitle('')
####################################################

""" 算法逻辑区 """
""" 定义按钮的信号的槽函数 """


def button_click():
    current_text = window.sender().text()  # 获得按当前钮信号发送者的文本
    current_content = display_label.text()  # 获得显示窗口的文本
    print(current_content, ', ', current_text)  # 测试
    # 逻辑区
    if current_text == 'C':  # 清除屏幕
        display_label.setText('0')
    elif current_text == 'Del':  # 退格
        if len(current_content) == 1:  # 内容长度为1，显示0
            display_label.setText('0')
        else:  # 删除最后一个==保留除了最后一个
            display_label.setText(current_content[:-1])  # 倒数第一个的索引‘-1’
    elif current_text == '=':  # 计算结果
        if current_content == '0':  # 显示0，结果0
            display_label.setText('0')
        else:  # 计算显示的内容
            formula_line = current_content + current_text + '\n'  # 这里的 current_text 为 ‘=’ 号
            result_line = eval(current_content)
            display_label.setText(formula_line + str(result_line))
    else:  # 正常的点击按钮，情况1：0，情况2：非0
        if current_content == '0':
            display_label.setText(current_text)
        else:
            display_label.setText(current_content + current_text)


""" 界面区 """
""" 定义网格组件名称+坐标列表 """
names = ['C', '(', 'Del', '+',
         '7', '8', '9', '-',
         '4', '5', '6', '*',
         '1', '2', '3', '/',
         '0', '.', ')', '=']

poses = [(1, 0), (1, 1), (1, 2), (1, 3),
         (2, 0), (2, 1), (2, 2), (2, 3),
         (3, 0), (3, 1), (3, 2), (3, 3),
         (4, 0), (4, 1), (4, 2), (4, 3),
         (5, 0), (5, 1), (5, 2), (5, 3)]

""" 创建网格全局布局，并加入到窗口中 """
whole_layout_grid = QGridLayout()
window.setLayout(whole_layout_grid)

""" 创建计算器显示窗口label对象 """
display_label = QLabel('0')  # 设置默认显示文本 0
# 添加窗口背景色
display_label.setStyleSheet('background-color:gray;')
# 设置窗口高度
display_label.setFixedHeight(100)
# 设置初始文本显示未知
display_label.setAlignment(Qt.AlignRight | Qt.AlignBottom)
# 设置初始文本字体和大小，并将这个设置应用于dispaly_label组件
font = QFont('宋体', 15)
display_label.setFont(font)
# 将显示窗口组件添加到整体布局中, from_row, from_col, row_span, col_span
whole_layout_grid.addWidget(display_label, 0, 0, 1, 4)

""" 在下一行添加所有的按钮 """
# 使用元组的打包 zip 与拆包操作
for name, pos in zip(names, poses):  # 拆包，打包，两包元素一一对应
    # 对每一个name,pos创建按钮
    button = QPushButton(name)
    # 设置宽度+高度
    button.setFixedSize(50, 40)
    # 设置点击事件（广播），并连接槽函数
    button.clicked.connect(button_click)
    # 设置 C，=按钮颜色
    if name == 'C':
        button.setStyleSheet('color:red')
    elif name == '=':
        button.setStyleSheet('background-color:orange')
    # 将按钮组件添加到整体布局中
    whole_layout_grid.addWidget(button)

####################################################
# 设置大小
window.resize(480, 640)
# 展示窗口
window.show()
# 等待窗口停止,退出操作
sys.exit(app.exec())
####################################################

# def test():
#     l = [0, 1, 2, 3]
#     print(l[:-1])  # 0, 1, 2

# if __name__ == '__main__':
#     test()
