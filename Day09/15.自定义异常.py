# 自己定义异常
# 自己抛出异常
# 网络框架  sendRequest()  网页不存在 404 抛出异常PageNotFondError 服务器错误 500 ServerError
# 1.自定义异常
# 2.在合适的时候抛出异常
# 所有的异常基本上都是继承自Exception
# IndexError
# KeyError
# ValueError

class ServerError(Exception):
    def __init__(self,msg):
        self.msg = msg

    def __str__(self):
        return self.msg

a = 10
b = 0
try:
    if b==0:
        # 抛出自定义的异常
        raise ServerError('除0异常')
    result = a/b
except ServerError as error:
    print('出现了异常',error)


