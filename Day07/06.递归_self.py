count = 0
def fact(n):
    '''
    求n的阶乘
    :param n:
    :return:
    '''
    global count
    count +=1  # 如果不加 global unresolved reference 'count'
    print(count)

    if n<1:
        return 0
    if n==1:
        return 1
    else:
        # n*(n-1)的阶乘
        return n*fact(n-1)

result = fact(996)
print(result)