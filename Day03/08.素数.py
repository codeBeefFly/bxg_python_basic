'''
列出1~1000内的所有素数
分析:
1.找到所有的1到1000以内的数据(for)
2.判断是否是素数
    2: 1 2 素数
    3: 1 3 素数
    4: 1 2 4 不是素数
    5: 1 5 素数
    5: 2..4
    判断从2到比当前数小1的数据,是否可以整除,有可以整除的数,不是素数
    10 :1 2

    10:假设能够被一个数据整a除   10//a = 最小2   10//2=5 6
    11//2 = 5
'''
# 高效:时间复杂度
# 2  3:1   999
# 1.找到所有的1到1000以内的数据(for)
for ele in range(2,1001):
    # 判断从2到比当前数小1的数据,是否可以整除,有可以整除的数,不是素数
    for a in range(2,ele//2+1):
        if ele%a==0:
            # 不是素数,退出当前内部循环
            break
    else:
        print(ele)