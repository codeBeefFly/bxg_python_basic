"""
1. 练习1: 定义一个整数变量age，编写代码判断年龄是否正确
    要求人的年龄在 0-120 之间
2. 练习2: 定义两个整数变量python_score、c_score，编写代码判断成绩
     要求只要有一门成绩 > 60 分就算合格

"""
# age = int(input('请输入年纪'))
# if age>0 and age<120:
#     print('合法年纪')

python_score = float(input('请输入python成绩:'))
c_score = float(input('请输入c成绩'))
if python_score>=60 or c_score>=60:
    print('成绩合格')