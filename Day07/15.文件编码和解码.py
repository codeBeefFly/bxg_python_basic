# 打开文件
f = open('d.txt','w',encoding='utf-8')
# print(f.encoding)
# 写入数据
f.write('中国')
# 关闭文件
f.close()

# 建议开发时使用 utf-8编码方式

# a = 10
# print(type(a))
# a = 'UR机器人'
# print(type(a))
# a = [1,2,3]
# print(type(a))
