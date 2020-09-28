# def func(**kwargs):
#     print(kwargs)
#
# d = {'name':'ABB机器人','load':30}
# # func(name='Abb',load=30)
# # func(10)
# # 将字典拆分成不存在的关键字参数
# func(**d)

def sum(*args):
    # ({'name':'ABB机器人','load':30},)
    print(args)

d = {'name':'ABB机器人','load':30}
# sum(10,20,30)
# sum(d)
# 字典可以通过一个*拆分,拆分的是key 可以传递给可变参数args
sum(*d)