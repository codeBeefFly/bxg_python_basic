# 打开
f = open('a.txt','r+')
# 写入数据
# f.write('hello world')

l = ['UR机器人','AuBo机器人','ABB机器人']
# l = [10,20,30]
# 写入容器中数据
f.writelines(l)
# 关闭
f.close()

