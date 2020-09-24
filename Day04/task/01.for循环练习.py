'''
1.打印字符串'hello world'中除了'w'之外的每一个元素
2.打印字符串'hello world'中第一个'o'出现之前(不包含第一个'o')的所有元素
3.打印字符串'hello world'中第三个'l'出现之前(不包含第三个'l')的所有元素

'''
# 1.打印字符串'hello world'中除了'w'之外的每一个元素
# str = 'hello world'
# for ele in str:
#     if ele=='w':
#         continue
#     print(ele)


# 2.打印字符串'hello world'中第一个'o'出现之前(不包含第一个'o')的所有元素
# str = 'hello world'
# for ele in str:
#     if ele=='o':
#         break
#     print(ele)
#
# 3.打印字符串'hello world'中第三个'l'出现之前(不包含第三个'l')的所有元素
str = 'hello world'
# 记录出现的l的次数
count = 0
for ele in str:
    if ele == 'l':
        count+=1
        if count==3:
            break
    print(ele)
