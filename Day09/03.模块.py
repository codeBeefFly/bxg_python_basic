'''---------------------- 第一种使用模块方式 ----------------------'''
# # 使用utils中的模块
# import utils
#
# # 使用模块中的功能
# print(utils.name)
# result = utils.add(10,20)
# print(result)
# # 创建模块中的对象
# robot = utils.Robot()
# robot.movej()

'''---------------------- 第二种  form 模块 import 功能 ----------------------'''
# 导入模块中单个功能
# from utils import name,add,Robot
# 全部导入模块的功能

# from utils import *
#
# print(name)
# result = add(10,20)
# print(result)
# robot = Robot()
# robot.movej()

'''---------------------- 模块的冲突 ----------------------'''
from utils1 import name as utils1_name
from utils2 import name as utils2_name
print(utils2_name)