# 第一个参数 不是文件名,文件路径
# 绝对路径:缺点:一旦工程位置发生变化,就需要重新确定路径
# f = open('D:\\codespace\\robot\\python\\course\\python4\\Day07\\test\\d.txt')

'''---------------------- 相对路径 ----------------------'''
# 打开a.txt
# 当前目录
# 上一级目录
# 当前目录:Day07
# f = open('./a.txt')
# 如果文件在当前目录,可以省略./
# f = open('a.txt')
# f.close()

# 打开d.txt
# f = open('./test/d.txt')
# f.close()