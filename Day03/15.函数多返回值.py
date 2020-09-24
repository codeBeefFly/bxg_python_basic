# 定义函数,求两个数的和以及两个数的差
def cacl(a,b):
    sum = a+b
    result = a-b
    return sum,result # 组包

# result = cacl(10,20)
a,b = cacl(10,20)
print(a,b)