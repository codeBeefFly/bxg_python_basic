# 模块内置属性 __name__
# 如果在当前模块执行  __main__
# 如果通过导入执行  模块名
# 入口函数

# 导入其实就会将模块中的代码执行一遍
import utils1

if __name__ == '__main__':
    result = utils1.add(10,20)
    print(result)
