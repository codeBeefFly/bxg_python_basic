'''
设计一个程序，实现str.split()方法的替换：
首先输入一个任意长度的字符串
其次输入一个字符，用以分割该字符串，并且分割后的字符串保存到一个列表中
不允许使用str.split()方法
最后打印出该字符串被分割成多少部分、以及这个列表
去掉分割出来的空字符串
如"1234r5678r90r"用r分割，则为["1234","5678","90"]
'''
# str = 'UR机器人helloAuBo机器人helloABB机器人hello安川机器人hello'
# # 获取所有的机器人名字
# # split 系统已经实现的功能
# l = str.split('hello')
# print(l)

# 定义功能
def mySplit(str,splitStr):
    '''
    对传入的字符串按照特定的字符进行分隔
    :param str: 需要分隔字符串
    :param splitStr: 分隔的字符串
    :return: 分割之后的结果列表
    '''
    # UR机器人helloAuBo机器人helloABB机器人hello安川机器人helloadfsf
    # hello
    # 1.定义保存结果的列表容器
    result = []
    # 定义需要查找的字符串
    rightStr = str[:]
    while True:
        # 2.查找分割字符串在字符串中的索引
        index = rightStr.find(splitStr)
        if index!=-1:
            # 3.切片 0:index 添加到结果的容器中
            leftStr = rightStr[:index]
            # 添加到结果容器中
            result.append(leftStr)
            # 4.切片 hello后的位置:最后 继续查找索引
            rightStr = rightStr[index+len(splitStr):]
        else:
            # 5.直到找不到索引 停下来 把最后一部分内容添加到结果列表中
            result.append(rightStr)
            # 停下来
            break
    return result


# 1.输入字符串
str = input('请输入字符串')
splitStr = input('请输入分割的字符串')
# 2.调用这个功能完成分隔
result = mySplit(str,splitStr)
print(result)
