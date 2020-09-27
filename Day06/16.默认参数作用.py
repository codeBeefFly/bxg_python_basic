# 默认参数的作用
# 网络请求代码
# python不支持方法重载(同函数名,不同函数参数)

def sendRequest(path,method='GET'):
    '''
    发送网络请求
    :param path: 请求路径
    :param method: 请求方式
    :return:
    '''
    print('请求路径:{},请求方式:{}'.format(path,method))

# 请求百度
sendRequest('http://www.baidu.com')
sendRequest('http://www.toutiao.com/login','POST')

# 头条 30 请求首页  请求详情  请求图片  登录  注册
# 请求方式:GET 25   POST 5
# 每一次GET请求都需要填写请求方式,很不方便

# # 方法重载:多个同名的函数  参数不同
# 十几个  二十几个方法重载
# def sendRequest(path):
#     '''
#     发送网络请求
#     :param path: 请求路径
#     :param method: 请求方式
#     :return:
#     '''
#     print('请求路径:{},请求方式:{}'.format(path,'GET'))
#
# def sendRequest(path,method):
#     '''
#     发送网络请求
#     :param path: 请求路径
#     :param method: 请求方式
#     :return:
#     '''
#     print('请求路径:{},请求方式:{}'.format(path,method))
#
# sendRequest('http://www.baidu.com')
# # sendRequest('http://www.toutiao.com/login','POST')