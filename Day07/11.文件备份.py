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
origalF = open(fileName,encoding='utf-8')
# 4.写入到复制的文件中(创建拷贝的文件  并且执行写入)
copyFile = open(copyName,'w',encoding='utf-8')
# 5.拷贝
# 一次性把文件读取到内存中 100M  1G 内存溢出
content = origalF.read()
copyFile.write(content)

