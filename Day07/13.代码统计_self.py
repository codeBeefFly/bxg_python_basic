'''
需求：
练习代码统计

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
fileName = input('请输入文件名：')
# 2.打开文件
file = open(fileName, encoding='utf-8')
# 3. 定义统计变量
code_lines, comment_lines, empty_lines = 0, 0, 0
# 3.1.按行读取+循环
line = file.readline()
while line:
    # comment line, 思路：除去首尾空格，以#起始
    if line.strip().startswith('#'):
        comment_lines += 1
    # empty line，思路：出去首尾空格，为空
    elif not line.strip():
        empty_lines += 1
    # code line，剩余的行
    else:
        code_lines += 1
    line = file.readline()

print('代码行：{}，注释行：{}，空行：{}'.format(code_lines, comment_lines, empty_lines))