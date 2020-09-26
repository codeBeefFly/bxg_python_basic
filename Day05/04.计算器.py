from PyQt5.QtWidgets import QWidget, QApplication, QGridLayout, QLabel, QPushButton
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
import sys

'''
网格布局:可以指定控件在哪一行哪一列展示  可以指定占用几行几列
'''
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


def btnClick():
    # 获取点击按钮的文字
    text = window.sender().text()
    # 获取原来展示的文字
    content = label.text()
    if text == 'C':
        # 清空
        label.setText('0')
    elif text == 'Del':
        # 删除一位
        # 如果当前只有一位数据,设置为0
        if len(content) == 1:
            label.setText('0')
        else:
            # 多位 删除后面的 '125'
            label.setText(content[:-1])
    elif text == '=':
        if content == '0':
            label.setText('0')
        else:
            # 计算结果
            # 上一行
            preLine = content + text + '\n'
            # 下一行
            resultLline = eval(content)
            label.setText(preLine + str(resultLline))
    else:
        if content == '0':
            label.setText(text)
        else:
            # 在原来的基础上加上按钮文字 12
            label.setText(content + text)


# 创建PyQt程序(sys.argv 固定写法)
app = QApplication(sys.argv)
# 创建窗口
window = QWidget()
# 修改标题
window.setWindowTitle('计算器')


# 创建整体布局
wholeLayout = QGridLayout()
# 设置布局
window.setLayout(wholeLayout)
# 结果显示的QLabel (全局变量)
label = QLabel('0')
# 添加背景颜色
label.setStyleSheet('background-color:grey;')
# 设置高度
label.setFixedHeight(100)
# 设置内容显示在右下角
label.setAlignment(Qt.AlignRight | Qt.AlignBottom)
# 设置显示的文本字体和大小
font = QFont('宋体', 15)
label.setFont(font)
# 参数1和2:从哪一行哪一列开始  参数3:占用行数  参数4:占用列数
wholeLayout.addWidget(label, 0, 0, 1, 4)
# 添加所有的按钮
for name, pos in zip(names, poses):
    # 创建按钮
    btn = QPushButton(name)
    # 设置宽度和高度
    btn.setFixedSize(40, 40)
    # 按钮点击事件
    btn.clicked.connect(btnClick)  # 信号通过广播方式传递
    # 颜色判断
    if name == 'C':
        # 设置字体颜色
        btn.setStyleSheet('color:orange')
    elif name == '=':
        # 设置背景颜色
        btn.setStyleSheet('background-color:orange')
    # 添加到网格布局中
    wholeLayout.addWidget(btn, pos[0], pos[1])

# for index in range(len(names)):
#     # 获取文字
#     name = names[index]
#     # 获取对应的位置
#     pos = poses[index]
#     # 创建按钮
#     btn = QPushButton(name)
#     # 添加到网格布局中
#     wholeLayout.addWidget(btn,pos[0],pos[1])


# 展示窗口
window.show()
# 等待窗口停止,退出操作
sys.exit(app.exec())
