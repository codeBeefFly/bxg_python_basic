"""
需求:
    收银员输入苹果的价格,单位:元/斤
    收银员输入用户购买苹果的重量,单位:斤
    计算并输出付款金额
"""
# 收银员输入苹果的价格,单位:元/斤
price = float(input('请输入苹果价格:'))
# 收银员输入用户购买苹果的重量,单位:斤
weight = float(input('请输入购买的重量:'))
# 计算并输出付款金额
money = price*weight
print(money)