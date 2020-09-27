"""
需求：
输入年月日：20180325
输入在当年的哪一天（第84天）

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
"""

# 1. 输入年月日（默认输入符合条件）
date = input('请输入年月日：')
# 2. 从输入的年月日字符串中分隔出 年 月 日
year = int(date[:4])
month = int(date[4:6])
day = int(date[6:])
# print(year, ', ', month, ', ', day)  # test
# 3. 根据年把当前前 每个月对应的天数 定义出来（平年+闰年）
month_day_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# 3.1 判断是否式闰年（普通闰年+世纪闰年），是，二月份为28天
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):  # 普通闰年？or 世纪闰年？
    month_day_list[1] = 29
    print('leep year!')
else:
    print('normal year!')
# 4. 循环从1月份到当前月 把之前每个月对应的天数加起来
total_days = 0
for past_month in range(1, month):
    total_days += month_day_list[past_month - 1]
print(total_days)
# 5. 天数再加上当前月已经经过的天数
total_days += day
print(total_days)
