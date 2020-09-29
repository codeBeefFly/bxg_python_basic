a = 10
b = 0
try:
    result = a/b
    print(result)
except:
    print('出现了异常')
else:
    print('没有异常')
    print(result)
finally:
    print('最终执行')