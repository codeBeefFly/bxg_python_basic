"""
1. 输入用户年龄
2. 判断是否满 18 岁 （>=）
3. 如果满 18 岁，允许进网吧嗨皮
4. 如果未满 18 岁，提示回家写作业

"""
# python没有{}确定作用域  是通过缩进来确定作用域
age = int(input('请输入年纪'))
if age>=18:
    print('可以进网吧')
else:
    print('回家写作业')