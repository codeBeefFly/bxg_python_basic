class Circle:
    def __init__(self):
        # 圆周率(圆周率不能在外部修改)
        self.PI = 3.1415926

    def getPI(self):
        return self.PI

# 创建对象
cicle = Circle()
# 直接访问属性
print(cicle.PI)
cicle.PI = 40
print(cicle.PI)
# cicle.getPI()=40

