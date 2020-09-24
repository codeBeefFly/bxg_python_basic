'''
1.系统里面有多个用户，用户的信息目前保存在列表里面
    users = ['root','westos']
    passwd = ['123','456']
2.用户登陆(判断用户登陆是否成功）
    1).判断用户是否存在
    2).如果存在
        1).判断用户密码是否正确
        如果正确，登陆成功，推出循环
        如果密码不正确，登录失败
    3).如果用户不存在
    登录失败

'''
# 后台的用户数据
users = ['root', 'westos']
passwd = ['123', '456']

# 2.用户登陆(判断用户登陆是否成功）
name = input('请输入用户名')
pwd = input('请输入密码')
# 用户是否存在
index = 0
# 是否找到用户名
hasUser = False

# if name in users:
#     print('存在')
# else:
#     print('不存在')

while index < len(users):
    if name==users[index]:
        hasUser = True
        # 判断是否密码合法
        # 合法密码
        legelPwd = passwd[index]
        if legelPwd==pwd:
            print('登录成功')
        else:
            print('密码不合法')

    index += 1

if not hasUser:
    print('没有找到用户')
