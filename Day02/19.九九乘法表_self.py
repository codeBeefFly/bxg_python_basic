# 先实现 九九*
index_max = 9
index = 0
while index < index_max:
    print('*' * index)
    index += 1



# 实现乘法表
index_max = 10
index = 1
while index < index_max:
    print('{} x {} = {}\t'.format(index, index, index) * index)
    index += 1

print('\n' + '*' * 100 + '\n')

row_max = 10
col_max = 10
row = 1
col = 1
# while row < row_max:
#     while col <= row:
#         print('{} x {} = {}\t'.format(row, col, row*col))
#         col += 1
#     print('\n')
#     row += 1

# while col < col_max:
#     while row <= col:
#         print('{} x {} = {}\t'.format(row, col, row*col))
#         row += 1
#     print('\n')
#     col += 1


# while col <= row:
#     while row < row_max:
#         print('{} x {} = {}\t'.format(col, row, row*col))
#         # col += 1
#         row += 1
#     print('\n')
#     # row += 1
#     col += 1
while row < row_max:
    col = 1
    while col <= row:
        print("{} x {} = {}\t".format(col, row, col*row), end='')
        col += 1

    print('\n')
    row += 1


#
# row_min = 1
# col_min = 1
# row = 9
# col = 9
# while row >= row_min:
#     col = row
#     while col <= row:
#         print('{} x {} = {}\t'.format(col, row, col*row), end='')
#         col -= 1
#     print('\n')
#     row -= 1

print('\n' + '*' * 100 + '\n')

row = 9
col = row
while row > 0 and row <= 9:
    col = row
    while col > 0:
        print('{} x {} = {}\t'.format(col, row, col*row), end='')
        col -= 1
    print('\n')
    row -= 1
