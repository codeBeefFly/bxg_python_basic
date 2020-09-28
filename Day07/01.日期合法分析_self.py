'''
需求:
判断用户输入的日期是否为有效日期

用户可以输入"20170327"格式的日期
判断是否是有效日期，如"20170229"不是有效日期，"20171345"不是有效日期

分析:
1.输入年月日日期
2.判断长度必须为8位,不为8位重新输入
2.如果不是纯数字,重新输入
3.分割出年 月 日
4.年只要大于0< <2021
5.月在1到12之间
6.日必须要在1和当前月日期最大之间   3  1-31  2020 2 1-29
7.如果都满足,说明日期满足条件
'''

month_day_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

while True:
    # 获得日期
    date = input('请输入日期：')
    if len(date) < 8:
        print('日期长度不够')
        continue
    elif not date.isdecimal():
        print('日期不是纯数字')
        continue
    elif date == 0:
        print('退出程序')
        break
    # 拆分日期
    year = int(date[:4])
    month = int(date[4:6])
    day = int(date[6:])
    # 判断是否是闰年
    if ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0):
        print('leap year')
        month_day_list[1] = 29
    else:
        month_day_list[1] = 28
    # 判断year (1900-2050)
    if year not in range(1900, 2051):
        print('year not in range 1900-2050')
        continue
    # 判断month (1-12)
    elif month not in range(1, 13):
        print('month not in range 1-12')
        continue
    # 判断天数 在 1-最大天
    # elif day not in month_day_list[month-1]:
    elif day not in range(1, month_day_list[month-1]+1):  # range 左包含，右不包含
        print('day not in range 1-max_days_in_month')
        continue
    else:
        print('日期为：{}年，{}月，{}号。'.format(year, month, day))
        continue