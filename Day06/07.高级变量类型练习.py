'''
需求:
完成字符串的逆序以及统计
设计一个程序，要求只能输入长度低于31的字符串，否则提示用户重新输入
打印如下内容:
您输入的字符串: ...
长度: ...
逆序后为: ...
字符统计结果: ...(afsfdsf)  a:1  f:3 s:2 d:1
zhangsanlisi

分析:
1.输入长度低于31的字符串，否则提示用户重新输入
2.您输入的字符串: ...
3.长度: ...(len)
4.逆序后为: ...  hello  olleh  ()
5.统计结果  字符统计结果: ...(afsfdsf)  a:1  f:3 s:2 d:1
                zlfdsllfdlw :z:1 l:4 f:2
'''
while True:
    # 1.输入长度低于31的字符串，否则提示用户重新输入
    str = input('请输入低于31位的字符串')
    # 判断长度
    if len(str) > 31:
        print('字符串不能超过31位')
        continue
    # 2.您输入的字符串: ...
    print('您输入的字符串:{}'.format(str))
    # 3.长度: ...(len)
    print('长度:{}'.format(len(str)))
    # 4.逆序后为: ...  hello  olleh  ()
    # newStr = str[len(str)-1::-1]
    # hello
    # newStr = str[-1::-1]
    newStr = str[::-1]
    print('逆序后为:{}'.format(newStr))
    # 5.统计结果  字符统计结果: ...(afsfdsf)  a:1  f:3 s:2 d:1
    '''---------------------- 第一种解决方案 ----------------------'''
    # # 定义集合保存不重复的字母
    # s = set()
    # # 计算每一个字母的个数
    # for ele in str:
    #     s.add(ele)
    # print('去重结果:',s)
    # # 结果保存在字典中
    # resultDict = {}
    # for ele in s:
    #     c = str.count(ele)
    #     resultDict[ele] = c
    # print(resultDict)
    '''---------------------- 第二种解决方案 ----------------------'''
    # afsafdsafsadfds
    # 定义字典保存结果 元素:个数
    resultDict = {}
    # 遍历字符串
    for ele in str:
        if ele not in resultDict:
            # 如果元素在字典中不存在,创建新的数据  元素:1
            resultDict[ele] = 1
        else:
            # 如果元素在字典中存在,数量加1  元素:2
            # resultDict[ele] = resultDict[ele]+1
            resultDict[ele] += 1

    print(resultDict)


