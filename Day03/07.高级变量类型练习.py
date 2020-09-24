'''
有3个盒子，现在箱子里有8个物品等待分配，
请编写程序:
1. 完成随机的分配
2. 获取盒子信息 (每个盒子中的物品个数，及分别是什么)

分析:
1.三个盒子(嵌套列表 盒子,盒子,盒子)  1
2.8个物品(列表)  2
3.遍历8个物品,随机找一个盒子放入这个物品
4.遍历3个盒子,获取个数以及盒子物品
'''
import random

# # 1.三个盒子(嵌套列表 盒子,盒子,盒子)  1
# boxes = [[], [], []]
# # 2.8个物品(列表)  2
# items = ['可乐', '积木', '酸奶', '牛奶', '矿泉水', '冰糖雪梨', '脉动', '咖啡']
# # 3.遍历8个物品,随机找一个盒子放入这个物品
# for item in items:
#     # 随机一个盒子的索引
#     index = random.randint(0, 2)
#     # 随机找一个盒子
#     box = boxes[index]
#     # 放入物品
#     box.append(item)
# # 清空物品列表
# items.clear()
# # 4.遍历3个盒子,获取个数以及盒子物品
# for box in boxes:
#     print('物品个数:{},物品:{}'.format(len(box),box))

'''--------------------- 分配之后  盒子不能有的空的 ---------------------'''
# 1.三个盒子(嵌套列表 盒子,盒子,盒子)  1
boxes = [[], [], []]
# 2.8个物品(列表)  2
items = ['可乐', '积木', '酸奶', '牛奶', '矿泉水', '冰糖雪梨', '脉动', '咖啡']
# 先往3个盒子中添加一个物品 遍历
for box in boxes:
    index = random.randint(0,len(items)-1)
    # 随机获取一个物品
    item = items[index]
    # 添加到这个盒子中
    box.append(item)
    # 删除添加的这个物品
    items.remove(item)

# 3.剩下的物品再随机分配
for item in items:
    # 随机一个盒子的索引
    index = random.randint(0, len(boxes)-1)
    # 随机找一个盒子
    box = boxes[index]
    # 放入物品
    box.append(item)
# 清空物品列表
items.clear()
# 4.遍历3个盒子,获取个数以及盒子物品
for box in boxes:
    print('物品个数:{},物品:{}'.format(len(box),box))