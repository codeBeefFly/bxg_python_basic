'''
1. 使用字典来存储一个物品的信息（商品名、商品颜色、商品重量），这些信息来自键盘的输入

2. 存储多个商品

分析:
1.输入商品名 商品颜色 商品重量
2.保存到系统中
'''
# 列表保存所有的商品
products = []
while True:
    # 1.输入商品名 商品颜色 商品重量
    name = input('请输入商品名:')
    color = input('请输入商品颜色:')
    weight = input('请输入商品重量:')
    # 保存商品
    product = {'name':name,'color':color,'weight':weight}
    # 存放商品
    products.append(product)
    print('商品存入成功')
    print(products)