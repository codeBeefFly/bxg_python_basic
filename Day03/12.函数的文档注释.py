'''
需求:
定义函数完成抓取整个流程的功能(移动到物品位置、抓取物品、离开物品)
'''
def crawl():
    '''
    这是一个抓取的功能
    :return:
    '''
    print('3D相机扫描确定物品位置')
    print('移动机械臂到物品上方')
    print('下去移到物品的位置')
    print('使用夹爪抓取物品')
    print('离开箱子')
    print('移动到另外一个箱子')

def glue():
    '''
    这是一个鞋底点胶的功能
    :return:
    '''
    print('2D视觉确定鞋底位置')
    print('opencv边缘检测,检测鞋底位置')
    print('获取鞋底边缘的gcode数据点')
    print('movep移动机器人,移动的时候点胶')


crawl()
glue()

