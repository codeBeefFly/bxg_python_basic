'''---------------------- 第一种定义方式 ----------------------'''
# from enum import Enum
# Week= Enum('Week', ('Sun', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'))
# print(Week.Sun)
# print(Week.Tue)
'''---------------------- 第二种方式 ----------------------'''
from enum import Enum

class Weekday(Enum):
    # 值必须要唯一
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6

# 他们代表一周七天
Sun = 0
Mon = 1
Tue = 2
Wed = 3
Thu = 4
Fri = 5
Sat = 6




print(Weekday.Sun)
def todo(weekDay):
    if weekDay==Weekday.Sun:
        print('休息')
    else:
        print('工作')
todo(Weekday.Mon)
