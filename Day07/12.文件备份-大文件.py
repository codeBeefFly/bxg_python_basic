'''
输入文件的名字，然后程序自动完成对文件进行备份
分析:
1.输入文件名a.txt
2.定义好复制之后的文件名
3.读取输入的文件
4.写入到复制的文件中
'''
# 1.输入文件名a.txt
fileName = input('请输入需要复制的文件名')
# 2.定义好复制之后的文件名
# a.txt a[复制].txt
# 09.文件写入.py  09.文件写入[复制].py
# 获取最后一个点的索引
index = fileName.rindex('.')
name = fileName[:index]
endName = fileName[index:]
copyName = name+'[复制]'+endName
# print(copyName)
# 3.读取输入的文件
origalF = open(fileName)
# 4.写入到复制的文件中(创建拷贝的文件  并且执行写入)
copyFile = open(copyName,'w')
# 5.拷贝
# 大文件拷贝 ,读取一部分 写入一部分  再读取一部分再写入一部分,知道没有数据为止
# 读取一行,写入一行  等到没有数据停止
line = origalF.readline()
while line:# 读取的数据不为空
    copyFile.write(line)
    # 再读取一行
    line = origalF.readline()

