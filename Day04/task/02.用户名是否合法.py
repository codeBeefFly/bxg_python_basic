'''
判断登录用户名是否合法(不能用正则表达式)
用户名是数字字母或者_,需要在3到20位,必须有2个或以上大写字母,2个或以上小写字母,3个或以上数字
hhew2383dW_fkf&E@^

分析:
1.hhew2383dW_fkf&E@^
2.len(用户名)是否在3到20位之间
3.定义三个容器保存 大写字母  小写字母  数字
4.遍历用户名,判断元素是否是数字字母或_,不是,密码不合法,是  统计个数
5.循环结束之后,判断数字 大写字母 和小写字母个数是否符合需求
'''
# 1.hhew2383dW_fkf&E@^
name = 'hhew2383dW_fkfE'
# 3.定义三个容器保存 大写字母  小写字母  数字
numberContainer = '0123456789'
upperContainer = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lowerContainer = 'abcdefghijklmnopqrstuvwxyz'
# 定义三个变量 记录大小写字母以及数字的个数
numberCount = 0
lowerCount = 0
upperCount = 0

# 2.len(用户名)是否在3到20位之间
if len(name) >= 3 and len(name) <= 20:
    # 目前合法
    # 4.遍历用户名,判断元素是否是数字字母或_,不是,密码不合法,是  统计个数
    for ele in name:
        if ele in numberContainer:
            numberCount += 1
        elif ele in upperContainer:
            upperCount += 1
        elif ele in lowerContainer:
            lowerCount += 1
        elif ele == '_':
            pass
        else:
            print('密码不合法,非法字符')
            # 跳出循环
            break
    else:
        if upperCount>=2 and lowerCount>=2 and numberCount>=3:
            print('用户名合法')
        else:
            print('用户名不合法,数字和字母个数不满足需求')

else:
    print('不合法,长度不合法')
