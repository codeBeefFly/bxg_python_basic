'''
需求:
判断登录密码'hhew2383dW_fkf&E@^'是否合法
要求:
1. 密码必须是数字、字母(大小写都可以)、和下划线,否则不合法
2. 如果密码合法,就输出'密码合法,可以登录'

'''
pwd = 'hhew2383dW_fkfE'
# 定义容器,把所有合法的字符先保存下来
legelChars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_'
# 1. 密码必须是数字、字母(大小写都可以)、和下划线,否则不合法
# 遍历密码字符串
# count = 0
# for ele in pwd:
#     # 判断当前这个元素是否合法
#     # 数字、字母(大小写都可以)、和下划线
#     if ele in legelChars:
#         # 当前这个字母合法
#         count+=1
#     else:
#         # 当前字符不合法
#         break # 不需要再判断了
#
# if count==len(pwd):
#     print('合法密码')

for ele in pwd:
    # 判断当前这个元素是否合法
    # 数字、字母(大小写都可以)、和下划线
    # if ele in legelChars:
    #     # 当前这个字母合法
    #     pass
    # else:
    #     print('密码不合法')
    #     # 当前字符不合法
    #     break  # 不需要再判断了
    if ele not in legelChars:
        print('密码不合法')
        break  # 不需要再判断了
else:
    print('密码合法')

