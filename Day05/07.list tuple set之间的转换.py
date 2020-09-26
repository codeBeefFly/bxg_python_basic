l = ['李阳','张三','李四','李阳']
# 统计不重名的人名
# list->set
s = set(l)
# print(s)
# set->list
newL = list(s)
print(newL)

t = tuple(s)
print(t)
