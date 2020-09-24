"""
计算 0 ~ 100 之间所有数字的累计求和结果
0+1
+2
+3
+4
+5
"""
# index = 0
# # 定义变量保存求和结果
# sum = 0
# while index < 101:
#     sum += index
#     index += 1
# print(sum)

"""
计算 0 ~ 100 之间 所有 偶数 的累计求和结果
"""

index = 0
# 定义变量保存求和结果
sum = 0
while index < 101:
    # 如果是偶数,才加
    if index%2==0:
        sum += index
    index += 1
print(sum)
