'''
任何类都最终继承自object
'''

class Father:
    pass

class Son(Father):
    pass

class GrandSon(Son):
    pass


class Robot:
    pass
gd = GrandSon()
# 继承关系图
# print(GrandSon.__mro__)
# Robot继承关系
print(Robot.__mro__)