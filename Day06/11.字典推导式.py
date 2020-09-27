'''
定义{"1":1,"2":4,'3':9,..,'10':100}这样的字典

'''
# str = '1'
# int('1')
# a = 1
# b = str(1)
# d = {str(key):key**2 for key in range(1,11)}
# print(d)

l1 = [1,2,3,4,5,6,7,8,9,10]
l2 = [101,102,103,104,105,106,107,108,109,110]
# 字典
# d = {key:value for key in l1 for value in l2}
d = {key:value for key,value in zip(l1,l2)}
print(d)
