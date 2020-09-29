def div(a,b):
    try:
        result = a/b
        return result
    # except:# 捕获到异常(所有的异常)  返回-1  代表错误
    # except ZeroDivisionError as error:# 只捕获除0异常  其它异常都不管
    #     print('异常:{}'.format(error))
    except Exception as error:# 捕获所有的异常 并且知道是什么异常
        print('异常:{}'.format(error))
        return -1

print(div(10, 0))
