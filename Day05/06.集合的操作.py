'''---------------------- 遍历 ----------------------'''
# s = {'UR机器人','Aubo机器人','安川机器人','UR机器人'}
# for ele in s:
#     print(ele)

'''---------------------- 不能获取一个元素 ----------------------'''
# s = {'UR机器人', 'Aubo机器人', '安川机器人'}
# 集合能不能获取一个元素? 没有索引,不能获取一个元素
# ele = s[0]
# print(ele)

'''---------------------- 添加一个元素 ----------------------'''
# s = {'UR机器人', 'Aubo机器人', '安川机器人'}
# 添加ABB机器人
# s.add('ABB机器人')
# print(s)
'''---------------------- 删除元素 ----------------------'''
s = {'UR机器人', 'Aubo机器人', '安川机器人'}
# remove删除
# remove删除安川机器人 删除元素不存在,报错
# s.remove('ABB机器人')
# print(s)

# discard 删除不存在 不做任何处理
# s.discard('ABB机器人')
# print(s)
