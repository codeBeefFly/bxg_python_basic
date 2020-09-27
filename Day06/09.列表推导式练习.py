 '''
请写出一段 Python 代码实现分组一个 list 里面的元素
比如 [1,2,3,...100]变成 [[1,2,3],[4,5,6]....]

分析:
1.创建1到100列表 推导式
2.把列表三个元素为一组拆分  放到新的列表中
'''
# 1.创建1到100列表 推导式
l = [ele for ele in range(1,101)]
# print(l)
# 2.把列表三个元素为一组拆分  放到新的列表中
# newL = [(ele,ele+1,ele+2) for ele in range(1,101) if ele%3==1]
# print(newL)

# newl = [[i,i+1,i+2] for i in range(1,100) if i% 3==1]
# newl.append([100])
# print(newl)

# 0   3       6     9 99-102
# 1 2 3 4 5 6 7 8 9
# 传递列表  三个一组  最后不足三个为最后一组
newl = [l[ele:ele+3] for ele in range(len(l)) if ele%3==0]
print(newl)