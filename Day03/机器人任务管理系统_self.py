"""
需求：

最快速度，分析作业代码，
实现作业代码
理解代码构建思路

开始练习代码的重用思维，即，能复制粘贴就不用手写
非算法代码模板化，即，能少写就少写

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

# 定义全局变量：列表 l，用来存储客户列表
l = []

def printMenu():
    """
    主功能函数：显示任务菜单
    :return: None
    """
    print("*" * 50)
    print("欢迎使用[jacob_made机器人任务管理系统]v1.0")
    print()
    print("1. 新建任务")
    print("2. 显示所有任务")
    print("3. 查询任务")
    print()
    print("0. 退出系统")
    print("*" * 50)


def change_current_card_task(task_card):
    """
    次次功能函数：修改当前 task_card 中的 task_name, task_type
    :param task_card: 当前任务列表
    :return: None
    """
    new_task_name = input("请输入新的任务名:\t")
    new_task_type = input("请输入新的任务类型:\t")
    # 修改
    task_card[1] = new_task_name
    task_card[2] = new_task_type


def delete_current_card(task_card):
    """
    次次功能函数：在全局任务列表中删除当前的任务列表
    :param task_card: 当前任务列表
    :return:
    """
    if task_card in l:
        l.remove(task_card)


def handleCard(task_card):
    """
    次功能函数：循环处理当前任务（1-修改，2-删除，0-退出）
    :param task_card:
    :return: None
    """
    while True:
        choice = int(input("请输入对当前任务的操作：1.修改/ 2.删除/ 0.返回上一级:\t"))
        if choice == 1:
            change_current_card_task(task_card)
            break
        elif choice == 2:
            delete_current_card(task_card)
            break
        elif choice == 0:
            break
        else:
            print("请输入对当前任务的正确操作：1.修改/ 2.删除/ 0.返回上一级:\t")


def queryCard():
    """
    主功能函数：查询全局列表中的任务
    :return: None
    """
    # 思路，使用for查找l中的对应任务，找到打印，没找到，打印没找到
    print("您选择的功能是: 3，功能：查询任务")
    query_name = input("请输入查询的任务名:\t")
    # 查询任务，在 l-task_card-task_card[1] 中，查询过程中打印所有任务
    for task_card in l:
        print(task_card)
        if task_card[1] == query_name:
            # 打印找到的任务
            # 打印表头
            print("任务名\t任务类型\t任务数据")
            # 开始横线
            print('-' * 50)
            task_name = task_card[1]
            task_type = task_card[2]
            # 打印数据
            print(task_name, '\t', task_type, '\t', id(task_card))
            # 结束横线
            print('-' * 50)
            # 选择该如何处理当前任务（修改，删除）
            handleCard(task_card)
            break
    else:
        print("没有查询到包含此任务的任务卡")


def appendCard():
    """
    主功能函数：在全局任务列表中添加新任务
    :return: None
    """
    # 界面
    print("你选择的功能是: 1，功能：新建任务")
    task_name = input("请输入任务名:\t")
    task_type = input("请输入任务类型:\t")
    # 创建一个任务卡列表对象，对象中元素[客户在列表中序号，任务名，任务类型]
    task_card = [len(l), task_name, task_type]
    # 将客户添加到全局任务列表中
    l.append(task_card)


def showAllCards():
    """
    TODO
    :return:
    """
    # 界面
    print("你选择的功能是: 2，功能：显示全部任务")
    # 打印表头
    print("任务序号\t任务名\t任务类型\t任务数据")
    # 开始横线
    print('-' * 50)
    # 任务信息
    for task_card in l:
        task_seq = task_card[0]
        task_name = task_card[1]
        task_type = task_card[2]
        print(task_seq, '\t', task_name, '\t', task_type, '\t', id(task_card))
    # 结束横线
    print('-' * 50)


# 代码主体，循环显示页面
while True:
    # 打印菜单
    printMenu()
    # 接收操作类型输入
    choice = int(input("请输入执行的操作:\t"))
    # 判断输入类型，并执行不同操作
    # 0-退出系统，1-新建任务，2-显示全部任务，3-查询用户
    if choice == 0:
        break
    elif choice == 1:
        appendCard()
    elif choice == 2:
        showAllCards()
    elif choice == 3:
        queryCard()
    else:
        print("请输入正确的操作(0-退出系统，1-新建任务，2-显示全部任务，3-查询用户)")

print(len(l))