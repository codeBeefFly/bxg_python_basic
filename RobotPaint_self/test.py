def scale(x, y):
    # 疑问？？？可以查看机器人运动学中的平移旋转，问老师
    x = 0.3 - 0.6 * x / 640
    y = -0.5 + 0.4 * y / 480
    return  x, y

if __name__ == '__main__':
    print('point(0, 0)::\t', scale(0, 0))
    print('point(0, 480)::\t', scale(0, 480))
    print('point(640, 480)::\t', scale(640, 480))
    print('point(640, 0)::\t', scale(640, 0))