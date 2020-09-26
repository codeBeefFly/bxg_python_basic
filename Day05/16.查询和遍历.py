# countries = {'China': '中国', 'America': '美国', 'England': '英国'}
# 查询中国
# value = countries['France']
# print(value)
# value = countries.get('France')
# print(value)

'''---------------------- 遍历 ----------------------'''
countries = {'China': '中国', 'America': '美国', 'England': '英国'}
# 打印的是key
# for ele in countries:
#     print(ele,countries[ele])

# 打印所有的values
# for value in countries.values():
#     print(value)

# 打印所有的key
# for key in countries.keys():
#     print(key)

# 打印所有的key和value
for key,value in countries.items():
    print(key,value)