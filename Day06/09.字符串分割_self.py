"""
需求：
根据需求定义字符串分割函数

思路
1. 定义保存结果的列表容器
2. 查找分割字符串在字符串中的索引
3. 切片 0：index 添加到结果的容器中国
4. 切片 hello 后的位置：最后继续查找索引
5. 直到找不到索引 停下来 把最后一部分内容添加到结果列表中
"""

# 定义功能函数
# def my_split(src_str, split_pattern):
#     """
#     对传入的字符串按照特定的字符进行分割
#     :param src_str: 传入的字符串
#     :param split_pattern: 分割的字符串
#     :return: 分割之后的结果
#     """
#     str_list = []
#     while True:
#         tmp_index = src_str.find(split_pattern)
#         tmp_str = src_str[:tmp_index]
#         remain_str = src_str[tmp_index:]

# 定义功能函数
def my_split(src_str, split_pattern):
    """
    对传入的字符串按照特定的字符进行分割
    :param src_str: 传入的字符串
    :param split_pattern: 分割的字符串
    :return: 分割之后的结果
    """
    # 定义结果列表
    result_list = []
    # 右字符串
    right_str = src_str[:]
    # 循环
    while True:
        # 查找分隔符索引
        split_index = right_str.find(split_pattern)
        if split_index != -1:
            # 通过查找分割字符索引，取得左字符串
            left_str = src_str[:split_index]
            # 取得右字符串，在分割符后
            right_str = right_str[split_index + len(split_pattern):]
            # 将左字符串添加到结果列表中国
            result_list.append(left_str)
        else:
            # print('没有找到分隔符')
            # 直到找不到索引，停下来，把最后一部分内容添加到结果列表中
            result_list.append(right_str)
            break
    return result_list

def test_find(src_str, target):
    return src_str.find(target), len(target)

# 定义字符串
src_str = input('请输入字符串：')
# 定义分割符
split_pattern = input('请输入分割符：')
# 结果
result_str = my_split(src_str, split_pattern)
print(result_str)

print(test_find(src_str, 'hello'))