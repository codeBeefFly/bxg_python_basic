# # 机器人类
# class Robot:
#     # 定义Robot类, 定义成员属性name和type
#     def __init__(self):
#         # 成员属性
#         self.name = 'UR机器人'
#         self.type = 'UR3'

'''---------------------- 每一个机器人的属性值都不一样 ----------------------'''
# 机器人类
class Robot:
    # 定义Robot类, 定义成员属性name和type
    def __init__(self,name,type):
        # 成员属性
        self.name = name
        self.type = type


# 创建对象
robot = Robot('UR机器人','UR3')# 相当于执行了__init__方法
# 通过对象访问属性
print(robot.name)
print(robot.type)

# robot2 = Robot('AuBo机器人','AuBo i5')
# print(robot2.name)
# print(robot2.type)
robot2 = robot
robot2.name = 'ABB'
# print(robot2.name)
print(robot.name)

# l = [1,2,3]
# ll = l
# ll.append(4)
# print(l)