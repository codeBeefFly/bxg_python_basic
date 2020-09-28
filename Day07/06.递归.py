'''
使用递归求n的阶乘

分析:
阶乘:  5的阶乘 5*4*3*2*1  10的阶乘:10*9*8*..*1
5的阶乘:
5 * (4*3*2*1)
5的阶乘=5*(5-1)的阶乘
10的阶乘:10*(10-1)的阶乘

n的阶乘:n*(n-1)的阶乘
'''
# def func(n):
#     result = 1
#     for i in range(1,n+1):
#         result *=i
#     return result
#
# print(func(1000))

# 递归层级比较深容易内存溢出:996
# go:9万多次  kotlin:6万多次
# 10 函数层层调用 内存空间 内存溢出  100M
count = 0
def fact(n):
    '''
    求n的阶乘
    :param n:
    :return:
    '''
    global count
    count +=1
    print(count)

    if n<1:
        return 0
    if n==1:
        return 1
    else:
        # n*(n-1)的阶乘
        return n*fact(n-1)

result = fact(1000)
print(result)