# box = ['酸奶', '积木', '可乐', '盒子', '矿泉水', '可乐', '脉动']
# for ele in box:
#     print(ele)
# else:
#     print('执行了else')

# for ele in box:
#     if ele=='可乐':
#         continue
#     print(ele)
# else:
#     print('执行了else')


# 如果没有执行break,还会执行else中的语句
box = ['酸奶', '积木', '可乐', '盒子', '矿泉水', '可乐', '脉动']
# 只要循环中执行了break,就不再执行else中的语句了
for ele in box:
    if ele=='冰糖雪梨':
        break
    print(ele)
else:
    print('执行了else')
