'''
输入一个文件名,统计文件中代码行数、注释行数、空行数
并输出代码以及注释

分析:
1.输入统计的文件名
2.打开文件
3.按行读取
4.定义三个变量保存代码数  注释数 空行数
5.判断这一行是代码  注释 空行
    注释:去空白,是否以#开头
    空行:去空白 是否是空
    其它:代码
'''
# 1.输入统计的文件名
fileName = input('请输入需要统计的文件名')
# 2.打开文件
f = open(fileName,encoding='utf-8')
# 3.按行读取
line = f.readline()
# 4.定义三个变量
codeLines = 0
commandLines = 0
emptyLines = 0
while line:
    # 5.判断这一行是代码  注释 空行
    if line.strip().startswith('#'):
    #     注释:去空白,是否以#开头
        commandLines +=1
    elif not line.strip():
    #     空行:去空白 是否是空
        emptyLines+=1
    else:
    #     其它:代码
        codeLines+=1
    # 读取下一行
    line = f.readline()
print('代码行数:{},注释行数:{},空行数:{}'.format(codeLines,commandLines,emptyLines))