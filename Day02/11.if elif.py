"""
根据不同的场景选择不同的机器人移动操作
提示工作人员输入机器人操作的场景，机器人根据不同的场景选择不同的移动方式执行移动操作
"""
# 执行效率
# 代码是否简洁
scences = input('请输入工作场景:')
# if scences=='过来':
#     print('movej移动')
# elif scences=='下去':
#     print('movel移动')
# elif scences=='上去':
#     print('movel移动')
# elif scences=='离开':
#     print('movej移动')
# else:
#     print('请重新输入')
#

if scences=='过来' or scences=='离开':
    print('movej移动')
elif scences=='下去' or scences=='上去':
    print('movel移动')
else:
    print('请重新输入')

