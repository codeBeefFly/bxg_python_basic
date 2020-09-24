# 定义函数,求两个数和,拿到这个结果
def sum(a,b):
    result = a+b
    # 返回给调用者结果
    return result

def myMax(a,b):
    if a>b:
        return a
    else:
        return b

# result = sum(10,20)
# print(result)

max = myMax(10,20)
print(max)
