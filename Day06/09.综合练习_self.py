"""
需求：
判断用户输入的日期是否为有效日期

用户可以输入”20170327“等三种格式的日期
判断是否有效日期，如”20170229“不是有效日期，”20171345“不是有效日期

小知识：平年+闰年
平年和闰年的判断方法：不是闰年的年份就是平年。
闰年的判断方法：闰年分为普通闰年和世纪闰年。
普通闰年：能被4整除但不能被100整除的年份为普通闰年。
世纪闰年：能被400整除的为世纪闰年

思路：
1. 输入年月日（默认输入符合条件）
2. 从输入的年月日字符串中分隔出 年 月 日
3. 根据年把当前 每个月对应的天数 定义出来（平年+闰年）
4. 循环重1月份到当前月 把之前每个月对应的天数加起来
5. 天数再加上当前月已经经过的天数

有效日期条件
1. 输入年月日
2. 判断长度必须为8位，不为8位重新输入
3. 分割出年月日
4. 年 (0, 2021)
5. 月 (1, 12)
6. 日在 (1, 当前月最大天数)
7. 如果满足，符合条件
"""
# date, total_days
month_day_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

while True:
    date = input('请输入日期：')
    # 判断长度
    if len(date) != 8:
        print('日期格式（yyymmdd）输入错误，请重新输入')
        continue
    elif not date.isdecimal():
        print('日期必须为纯数字')
        continue
    elif date == '0':
        print('退出程序')
        break
    # 取得 年，月，日，要把 str -> int
    year = int(date[:4])
    month = int(date[4:6])
    day = int(date[6:])
    # 定义三个flag
    flag_year, flag_month, flag_day = True, True, True
    # 判断年 (0, 2021)
    if year not in range(1900, 2021):
        flag_year = False
        print('year error')
    # 判断月 (1-12)
    if month not in range(1, 12):
        flag_month = False
        print('month error')
    # 判断日 (1-最大）
    # 创建天数列表，并判断是否闰年
    # month_day_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    flag_leap_year = False
    if (month in [1, 3, 5, 7, 8, 10, 12]) and (day != 31):
        flag_day = False
    elif ((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)):
        print('leap year')
        if day != 29:
            flag_day = False
    elif day != 28:
        flag_day = False

    print(flag_year, '\t', flag_month, '\t',flag_day)
    print(flag_year and flag_month and flag_day)
    # if (flag_year and flag_month and flag_year):  # 有一个为 False
    if (not flag_year) or (not flag_month) or (not flag_day):
        print('日期格式（yyymmdd）输入错误，请重新输入')
        continue
    else:
        print('输入的日期为{}年, {}月, {}日。'.format(year, month, day))
        break

