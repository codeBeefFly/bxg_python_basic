'''
求第n个斐波那契数
1 1 2 3 5 8 13
分析:
1.第一个和第二个斐波那契数列都是1
2.从第三个开始,都是前面两个斐波那契数列的和
第n个斐波那契梳理  第n-1+第n-2
'''
def func(n):
    '''
    求第n个斐波那契数列
    :param n:
    :return:
    '''
    if n<1:
        return 0

    if n==1 or n ==2:
        return 1
    else:
        return func(n-1)+func(n-2)


print(func(7))