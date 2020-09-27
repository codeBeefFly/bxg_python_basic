'''
1.定义函数,求两个数的和
2.定义函数,求三个数的和
3.定义函数求任意个数的和

'''
# 1.定义函数,求两个数的和
# 2.定义函数,求三个数的和
# 3.定义函数求任意个数的和
# def add(a,b,c,d,e,f):
#     return a+b+c
#
# result = add(10,20,30,40,50,60,70)
# print(result)


# 可变参数*args
# 可变参数接收之后是元组类型
# 可变参数需要放到参数最后
def add(name,*args):
    # args是什么类型的数据?
    # 定义保存和的变量
    print(name)
    sum = 0
    # 遍历args 把数据加到和上
    for ele in args:
        sum += ele
    return sum

result = add('UR机器人',10,20,30)
print(result)