class Robot:
    def __init__(self):
        self.name = 'UR机器人'

    def func(self):
        # 返回name属性的值
        return self.name

robot = Robot()
result = robot.func()
print(result)