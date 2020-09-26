# eval 可以执行字符串中的表达式
# str = '10+20'
str = '(10+20)*(3-1)'
# 知道字符串中表达式执行结果
result = eval(str)
print(result)
# print(str)