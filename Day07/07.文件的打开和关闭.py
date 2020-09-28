# 打开a.txt
# 如果文件不存在,就报错
# f = open('c.txt','r')
# 如果不写模式  默认就是r模式
# f = open('a.txt')

# w模式打开 如果文件存在,就会覆盖 (慎用)
# w模式打开, 如果文件不存在,就会创建
# f = open('b.txt','w')

# 读写
# f = open('a.txt','r+')

# 读写  覆盖
# f = open('a.txt','w+')

# 关闭
f.close()