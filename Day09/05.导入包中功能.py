'''---------------------- import ----------------------'''
# import 包.模块
# import net.a.user as user
# # import numpy as np
# # import cv2 as cv
# user.login('张三','123')


'''---------------------- from import ----------------------'''
# 从包中导入模块
# from net.a import user
# from net.a.user import login,regist
# 从包中的模块导入功能
# from net.user import *
# login('张三','123')

'''---------------------- 模块重名 ----------------------'''
from net import user as net_user
from storage import user as sto_user
net_user.login('李四','123')
sto_user.save()