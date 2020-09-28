'''
写一个圆形类,传递圆的直径,定义方法求圆的周长

'''
'''
默认:属性和方法都是公有的  在外部都可以通过对象访问
私有:只能在类内部访问,不能在外部访问
如何私有化?
属性前加上__
私有化之后,外部不能访问这个属性,不能修改
'''
class Circle:
    def __init__(self,radius):
        # 半径
        self.radius = radius
        # 圆周率(圆周率不能在外部修改)
        self.__PI = 3.1415926

    def perimeter(self):
        return 2*self.__PI*self.radius


# 创建圆
circle = Circle(20)
# circle.PI  = 40
# print(circle.__PI)

# __age = 10
# 并不是修改内部的__PI属性,定义了新的属性__PI
# __PI = 40
circle.__PI = 40
print(circle.__PI)
# 周长
result = circle.perimeter()
print(result)

