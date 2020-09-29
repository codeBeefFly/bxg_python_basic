'''---------------------- IndexError ----------------------'''
# IndexError: list index out of range 角标越界
# l = [1,2,3]
# print(l[-5])

'''---------------------- KeyError ----------------------'''
# KeyError: 'weight' 键不存在
# d = {'name':'UR机器人','type':'UR3'}
# print(d['weight'])

'''---------------------- ValueError ----------------------'''
# ValueError: invalid literal for int() with base 10: 'a' 数据转换出错
# print(int('a'))

'''---------------------- AttributeError ----------------------'''
# AttributeError: 'Person' object has no attribute 'age' 类的属性或方法不存在
class Person:
    def __init__(self):
        self.name = '张三'

p = Person()
print(p.name)
print(p.age)