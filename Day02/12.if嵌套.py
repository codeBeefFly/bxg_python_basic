"""
1. 定义布尔型变量 has_ticket 表示是否有车票
2. 定义整型变量 knife_length 表示刀的长度，单位：厘米
3. 首先检查是否有车票，如果有，才允许进行 安检
4. 安检时，需要检查刀的长度，判断是否超过 20 厘米
     果超过 20 厘米，提示刀的长度，不允许上车
     如果不超过 20 厘米，安检通过
5. 如果没有车票，不允许进门

"""
# 是否有票 0 1234
has_ticket = int(input('请输入是否有票'))
# 刀的长度
knife_length = int(input('请输入刀的长度'))
if has_ticket:
    if knife_length>=20:
        print('不允许上车')
    else:
        print('允许上车')
else:
    print('没有票,不允许进门')