# finally特点:不管代码有没有异常都会执行,最后执行
# finally作用:文件关闭  数据库关闭 必须要执行的操作
# a = 10
# b = 0
# try:
#     result = a/b
#     print(result)
# except:
#     print('出现异常')
# finally:
#     print('执行了finally')

'''---------------------- 打开文件 ----------------------'''
try:
    # 打开
    f = open('a.txt')
    # 读写
    f.write('hello')
except:
    print('出现了异常')
finally:
    # 关闭(必须)
    f.close()
    print('关闭')