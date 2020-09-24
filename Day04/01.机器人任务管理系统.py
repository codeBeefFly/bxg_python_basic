# 定义数据类型保存任务 list str tuple
# 每一个任务是什么类型?
# 任务有哪些特点? [任务id,任务名,任务类型] id自增长
tasks = [[0,'装牛奶','码垛']]
# 每一次添加 记录当前id
taskId = len(tasks)


def printMenu():
    '''
    打印菜单
    :return:
    '''
    print('*' * 50)
    print('欢迎使用[机器人任务管理系统]V1.0')
    print()
    print('1.新建任务')
    print('2.显示所有任务')
    print('3.查询任务')
    print()
    print('0.退出系统')
    print('*' * 50)


def addTask():
    '''
    添加任务
    :return:
    '''
    global taskId
    # 打印功能提示
    print('您选择的功能是: 1')
    print('功能: 新建任务')
    # 输入任务名
    name = input('请输入任务名:')
    # 输入任务类型
    type = input('请输入任务类型:')
    # 把任务存储到系统中
    # 创建任务
    task = [taskId, name, type]
    # 添加任务
    tasks.append(task)
    # 增加id
    taskId += 1


def showAllTask():
    '''
    显示所有的任务
    :return:
    '''
    print('您选择的功能: 2')
    print('功能提示: 显示全部')
    # 显示表格表头
    print('任务名\t任务类型')
    # 打印横线
    print('-' * 50)
    # 查询所有的任务
    for task in tasks:
        # 获取当前的任务的名称
        name = task[1]
        # 获取任务的类型
        type = task[2]
        print('{}\t{}'.format(name, type))
    # 打印横线
    print('-' * 50)


def modifyTask(task):
    '''
    修改任务
    :param task: 需要修改的任务
    :return:
    '''
    # 输入修改之后的任务名
    name = input('请输入任务名:')
    # 输入修改之后的任务类型
    type = input('请输入任务类型:')
    # 修改
    task[1] = name
    task[2] = type


def deleteTask(task):
    '''
    删除指定的任务
    :param task:要删除的任务
    :return:
    '''
    # 列表删除元素
    tasks.remove(task)


def handleTask(task):
    '''
    对任务进行操作
    :param task:需要操作的任务
    :return:
    '''
    # 输入操作
    while True:
        type = input('请输入对任务的操作: 1.修改/ 2.删除/ 0.返回上一级:')
        if type=='1':
            modifyTask(task)
            # 跳出循环
            break
        elif type=='2':
            deleteTask(task)
            break
        elif type=='0':
            print('返回上一级')
            break
        else:
            print('请输入正确的操作,1.修改/ 2.删除/ 0.返回上一级')




def queryTask():
    '''
    查询任务
    :return:
    '''
    # 任务提示
    print('您选择的功能是: 3')
    print('功能: 查询任务')
    # 输入查询的任务名
    name = input('请输入查询的任务名:')
    # 根据任务名查询任务
    for task in tasks:
        if task[1]==name:
            # 查询到,显示查询的任务
            # 打印任务
            # 显示表格表头
            print('任务名\t任务类型')
            # 打印横线
            print('-' * 50)
            # 打印当前任务
            print('{}\t{}'.format(name, task[2]))
            # 打印横线
            print('-' * 50)
            # 操作任务(和查询任务没有直接关系)
            handleTask(task)
            # 找到任务,跳出循环
            break
    else:
        # 没有查询到,提示
        print('没有找到任务')


while True:
    # 打印菜单
    printMenu()
    # 输入操作
    type = input('请输入执行的操作:')
    # 判断操作类型
    if type == '1':
        addTask()
    elif type == '2':
        showAllTask()
    elif type == '3':
        queryTask()
    elif type == '0':
        print('退出系统')
        # 退出循环
        break
    else:
        print('请输入正确的操作(1.新建2.显示全部3.查询用户)')
