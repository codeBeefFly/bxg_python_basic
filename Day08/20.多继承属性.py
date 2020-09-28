'''
Mother类还具有money属性
Father类还具备wage工资属性

'''
class Mother:
    def __init__(self):
        self.money = 9500

class Father:
    pass
    # def __init__(self):
    #     self.wage = 10000

# 定义Son类
class Son(Father,Mother):
    pass

# 创建Son对象
son = Son()
print(son.money)
# print(son.wage)