'''
考试成绩的问题：提示用户输入成绩，判断是属于哪个水平，将结果打印到控制台。
 60以下不及格，60分以上为及格，70分至80分为合格，80分至90分为良好，90分以上为优秀。
例如：
请输入考试成绩：85
你的成绩是 85 ，成绩良好

分析:
1.输入成绩
2.判断水平
'''
# 执行效率
# 代码是否简洁

# 1.输入成绩
score = float(input('请输入成绩'))
# 2.判断水平
# if score<60:
#     print('不及格')
# elif score>=60 and score<70:
#     print('及格')
# elif score>=70 and score<80:
#     print('合格')
# elif score>=80 and score<90:
#     print('良好')
# elif score>=90:
#     print('优秀')

if score>=90:
    print('优秀')
elif score>=80:# 隐藏  score<90
    print('良好')
elif score>=70:# score<80
    print('合格')
elif score>=60:# score<70
    print('及格')
else:# score<60
    print('不及格')
