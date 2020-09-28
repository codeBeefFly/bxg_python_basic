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
monthDays = [31,28,31,30,31,30,31,31,30,31,30,31]
while True:
    # 1.输入年月日日期
    date = input('请输入日期:')
    # 2.判断长度必须为8位,不为8位重新输入
    if len(date)!=8:
        print('日期必须为8位')
        continue
    # 2.如果不是纯数字,重新输入
    if not date.isdecimal():
        print('日期必须为纯数字')
        continue
    # 3.分割出年 月 日
    year = int(date[:4])
    month = int(date[4:6])
    day = int(date[6:])
    print(year,month,day)
    # 修改每个月天数
    if (year%4==0 and year%100!=0) or (year%400==0):
        monthDays[1] = 29
    else:
        monthDays[1] = 28
    # 4.年只要大于0< <2021
    if year<1 or year>2020:
        print('年不满足需求')
        continue
    # 5.月在1到12之间
    if month<1 or month>12:
        print('月必须在1到12之间')
        continue
    # 6.日必须要在1和当前月日期最大之间   3  1-31  2020 2 1-29
    maxDay = monthDays[month-1]
    if day<1 or day>maxDay:
        print('天数不满足')
        continue

    print('日期满足')
    break



