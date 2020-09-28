
class Father:
    def func1(self):
        print('func1')

class A(Father):
    # def func1(self):
    #     print('func1')

    def func2(self):
        print('func2')


class B(Father):
    # def func1(self):
    #     print('func1')

    def func3(self):
        print('func2')

# 创建B对象
b = B()
b.func1()


