def sendRequest(path,method):
    print('请求地址:{},请求方式:{}'.format(path,method))

# sendRequest('http://www.baidu.com','GET')
sendRequest(method='GET',path='http://www.baidu.com')
