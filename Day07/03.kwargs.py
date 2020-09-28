# def func(name,load):
#     print('机器人名字:{},机器人荷载:{}'.format(name,load))
#
# func(load=5,name='UR机器人')

# 不存在的关键字参数:将参数变成字典类型
def func(**kwargs):
    for key,value in kwargs.items():
        print(key,value)

# 不存在的关键字参数
func(name='AuBo机器人',load=5)


# def sendRequest(path,method='GET',body=None):
def sendRequest(**kwargs):
    # 有可能传递path 和method  有可能传path body method
    print('发送网络请求')

# sendRequest(path='http://www.baidu.com')
# sendRequest(path='http://www.baidu.com',method='GET')
sendRequest(path='http://www.baidu.com',method='GET',body='UR机器人')