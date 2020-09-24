row = 9
while row >0:
    col = 1
    while col <= row:
        print('{} * {} = {}\t'.format(col,row,col*row),end='')# 自动带换行
        col += 1
    # 当前行已经打印完成,需要换行
    print()
    row -= 1


