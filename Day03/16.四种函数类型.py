'''--------------------- 无参无返回值 ---------------------'''
def crawl():
    print('3D相机扫描确定物品位置')
    print('移动机械臂到物品上方')
    print('下去移到物品的位置')
    print('使用夹爪抓取物品')
    print('离开箱子')
    print('移动到另外一个箱子')

'''--------------------- 无参有返回值函数 ---------------------'''
# import random
# # 传感器
# def getTem():
#     '''
#     温度传感器获取温度
#     :return:
#     '''
#     tem = random.randint(0,100)
#     return tem
# tem = getTem()
# print(tem)

'''--------------------- 有参有返回值 ---------------------'''
# def myMax(a,b):
#     if a>b:
#         return a
#     else:
#         return b
'''--------------------- 有参无返回值 ---------------------'''
def crawl(param):
    '''
    这是一个抓取的功能
    :return:
    '''
    print('3D相机扫描确定物品位置')
    print('移动机械臂到物品上方')
    print('下去移到物品的位置')
    print('使用夹爪抓取物品')
    print('离开箱子')
    print('移动到另外一个%s'%param)