'''--------------------- 第一个三角形 ---------------------'''
'''
*
**
***
****
*****
'''
# index = 1
# while index < 6:
#     print('*'*index)
#     index += 1

'''--------------------- 第二个三角形 ---------------------'''
'''
*****
****
***
**
*
'''
# index = 5
# while index > 0:
#     print('*'*index)
#     index -= 1

'''--------------------- 第三个三角形 ---------------------'''
'''
*****
 ****
  ***
   **
    *
每一行 空格和*个数相加等于5
'''
index = 1
while index < 6:
    # 空格
    spaceC = index-1
    # *个数
    starC = 5-spaceC
    data = ' '*spaceC+'*'*starC
    print(data)
    index += 1
