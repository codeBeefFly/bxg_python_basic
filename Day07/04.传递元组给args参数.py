def sum(*args):
    print(args)
    # ((10, 20, 30, 40, 50),)c
    result = 0
    for ele in args:
        result += ele
    return result

# sum(10,20,30,40,50)
t = (10,20,30,40,50)
# 将元组拆分之后再传递
# sum(t[0],t[1],t[2])
result = sum(*t)
print(result)