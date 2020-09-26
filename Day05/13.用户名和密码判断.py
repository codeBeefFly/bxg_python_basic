'''
用户名和密码格式校验程序
要求从键盘输入用户名和密码，校验格式是否符合规则，如果不符合，打印出不符合的原因，并提示重新输入
用户名长度6-20，用户名必须以字母开头
密码长度至少6位，不能为纯数字，不能有空格

分析:
1.输入用户名
2.判断用户名是否符合需求,不符合需求,重新输入
3.用户名满足,输入密码
4.密码不满足,重新输入密码
5.用户名和密码输入符合需求,发送给服务器校验
'''
while True:
    # 1.输入用户名
    name = input('请输入用户名')
    # 2.判断用户名是否符合需求,不符合需求,重新输入
    # 用户名长度6-20
    # if not (len(name)>=6 and len(name)<=20):
    if len(name)<6 or len(name)>20:
        print('用户名必须在6到20位之间,请重新输入')
        continue
    # 用户名必须以字母开头
    if not name[0].isalpha():
        print('用户名必须以字母开头')
        continue
    # 条件都满足
    print('用户名输入正确')
    # 跳出用户名的循环
    break

# 3.用户名满足,输入密码
while True:
    pwd = input('请输入密码')
    # 密码长度至少6位
    if len(pwd)<6:
        print('密码的长度必须至少为6位')
        continue
    # 不能为纯数字
    if pwd.isdecimal():
        print('密码不能只包含数字')
        continue
    # 不能有空格 hello world
    if ' ' in pwd:
        print('密码不能有空格')
        continue
    # 密码可以
    print('密码输入成功')
    # 跳出密码的循环
    break

# 发送用户名和密码到服务器
print('开始登录')