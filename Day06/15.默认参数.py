str = 'UR机器人helloAuBo机器人hello安川机器人'
# 第三个参数就是默认参数
# newStr = str.replace('hello','haha')
# print(newStr)

'''---------------------- 默认参数 ----------------------'''
# 默认参数和普通参数顺序:普通参数在前  默认参数在后
def move(data,type='关节运动'):# type就是默认参数
    print('移动类型:{}'.format(type))

# # movej
# move('关节运动')
# # movel
# move('直线运动')
# move('直线运动')
move([1,2,3,4,5,6],'直线运动')