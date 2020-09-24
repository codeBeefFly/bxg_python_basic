"""
分析:
1.显示主菜单
2.新建任务
3.显示所有任务
    1.修改任务
    2.删除任务
4.查询任务


任务保存:
1.保存所有的任务:列表[]
2.每一个任务中:任务id、任务名、任务类型、任务末端关节位置[任务id,任务名,任务类型]
任务类型:1:关节移动  2:直线移动  3:movep
"""

# 定义系统保存任务的列表
l = []

def printMenu():
    """打印初始化提示菜单"""
    print("*" * 50)
    print("欢迎使用[机器人任务管理系统]V1.0")
    print()
    print('1.新建任务')
    print('2.显示所有任务')
    print('3.查询任务')
    print()
    print('0.退出系统')
    print("*" * 50)


def appendCard():
    """新建任务"""
    print("您选择的功能是:1")
    print("功能:新建任务")
    task = input("请输入任务名:")
    type = input("请输入任务类型:")
    # 定义当前用户的任务列表
    person = [len(l),task,type]
    # 任务保存到系统中
    l.append(person)


def showAllCards():
    """显示所有用户任务"""
    # 显示任务
    print("您选择的功能:2")
    print("功能提示:显示全部")
    # 打印表头
    print("任务名\t任务类型\t位置数据")
    # 开始横线
    print('-' * 50)
    # 任务信息
    for person in l:
        task = person[1]
        type = person[2]
        print(task, '\t', type)
    # 结束横线
    print('-' * 50)


# 修改任务
def changeCard(card):
    task = input("请输入任务名:")
    type = input("请输入任务类型:")
    # 修改
    card[1] = task
    card[2] = type


def deleteCard(card):
    """删除任务"""
    if card in l:
        l.remove(card)


def handleCard(card):
    while True:
        """操作任务:修改  删除"""
        type = int(input("请输入对任务的操作: 1.修改/ 2.删除/ 0.返回上一级:"))
        # 不同的类型处理方案
        if type==1:
            changeCard(card)
            break
        elif type==2:
            deleteCard(card)
            break
        elif type==0:
            break
        else:
            print("请输入正确的操作,1.修改/ 2.删除/ 0.返回上一级:")


def queryCard():
    """查询任务"""
    # 查询任务
    print('您选择的功能是:3')
    print('功能:查询任务')
    name = input('请输入查询的任务名:')
    # 查询当前任务
    for card in l:
        print(card)
        if card[1] == name:
            # 打印当前任务
            # 打印表头
            print("任务名\t任务类型\t位置数据")
            # 开始横线
            print('-' * 50)

            task = card[1]
            type = card[2]
            # 打印
            print(task, '\t', type)

            # 结束横线
            print('-' * 50)

            print("要修改的任务地址:",id(card))
            # 处理当前任务(修改  删除)
            handleCard(card)
            break
    else:
        print("没有查询到用户")


while True:
    printMenu()
    # 输入操作类型
    num = int(input("请输入执行的操作:"))
    # 输入的是0 需要停止循环
    if num==0:
        # 退出系统
        break
    elif num==1:
        # 新建任务(添加任务到系统中)
        appendCard()
    elif num == 2:
        showAllCards()
    elif num == 3:
        queryCard()
    else:
        print("请输入正确的操作(1.新建2.显示全部3.查询用户)")


print(len(l))

