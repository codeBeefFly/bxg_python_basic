"""
需求:
使用递归完成斐波那契数列算法的实现
算法：当前位的斐波那契数列值 = 前一位的斐波那契数列值 + 前前一位的斐波那契数列值
"""

def fibonacci(n):
    """
    输入n（第几个斐波那契数列），返回这个位置的斐波那契数列值
    1, 1, 2, 3, 5, 8, 13
    :param n: 斐波那契数列位置
    :return: 这个位置上的斐波那契数列值
    """
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n-2) + fibonacci(n-1)

position = 7
print('fibonacci value at {} is::{}'.format(position, fibonacci(position)))