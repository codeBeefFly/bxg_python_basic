'''
random.randint(start,end)随机整数，[start,end]
random.random()随机浮点数, [0,1)
random.uniform(start,end)随机浮点数, [start,end]
random.choice([])随机数组,返回单个元素
random.choices([])随机数组,返回列表

'''
import random
'''---------------------- random.randint(start,end)随机整数，[start,end] ----------------------'''
# print(random.randint(1, 10))
'''---------------------- random.random()随机浮点数, [0,1) ----------------------'''
# print(random.random())

'''---------------------- random.uniform(start,end)随机浮点数, [start,end] ----------------------'''
print(random.uniform(1, 4))
'''---------------------- random.choice([])随机数组,返回单个元素 ----------------------'''
l = ['张三','李四','王五']
# index = random.randint(0,len(l)-1)
# print(l[index])
print(random.choice(l))
print(random.choices(l))