'''
有10个球分别3红、3蓝、4白，现需要将这10个球放入这3个盒子，要求每个盒子至少有一个白球，
请用程序实现

分析:
1.定义三个盒子(嵌套列表)
2.3红(列表)
3.3蓝(列表)
4.4白(列表)
5.每个盒子至少有一个白球
    将每一个盒子先分配一个白球
6.把剩下的白球和其他球混合在一个再进行分配
'''
import random
# 1.定义三个盒子(嵌套列表)
boxes = [[],[],[]]
# 2.3红(列表)
reds = ['红1','红2','红3']
# 3.3蓝(列表)
blues = ['蓝1','蓝2','蓝3']
# 4.4白(列表)
whites = ['白1','白2','白3','白4']
# 5.将每一个盒子先分配一个白球
for box in boxes:
    # 随机白球的索引
    index = random.randint(0,len(whites)-1)
    # 根据索引获取一个白球
    whiteBall = whites[index]
    # 添加到盒子中
    box.append(whiteBall)
    # 从白球中删除这个球
    del whites[index]

# print(boxes)
# print(whites)
# TDD 开发 test driver 测试驱动开发 test driver development

# 6.把剩下的白球和其他球混合在一个再进行分配
newL = reds+blues+whites
# 遍历球列表
for ball in newL:
    # 随机获取盒子的索引
    index = random.randint(0,len(boxes)-1)
    # 根据这个索引获取盒子
    box = boxes[index]
    # 添加球到盒子中
    box.append(ball)

# 清空球的盒子
newL.clear()

print(boxes)

