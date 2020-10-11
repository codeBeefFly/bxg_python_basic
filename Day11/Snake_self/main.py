"""
需求：
以最快速度学习游戏代码编程思路，架构，忽略函数细节
理解思路+复制拷贝+运行调试+更新博客
"""
import sys
import random

import pygame
from pygame.locals import *

from local import *


def terminal():
    """
    退出游戏+程序
    :return:
    """
    # 在事件列表中获取特定事件，比如X或esc（更快些）
    event = pygame.event.get(QUIT)
    if event:
        # 退出pygame
        pygame.quit()
        # 退出程序
        sys.exit()


def show_tip():
    """
    加载提示文字
    :return:
    """
    # 加载提示文字，使用smallFont根据设定渲染一段文字，结果赋值与tipSurface
    tipSurface = smallFont.render('Press a key to play', True, RED)
    # 展示提示,将tipSurface上传到window
    window.blit(tipSurface, (WINDOWWIDTH - 200, WINDOWHEIGHT - 50))


def draw_grid():
    """
    绘制游戏界面网格
    :return:
    """
    for col in range(1, CELLWIDTH):  # window-width / cell-size
        pygame.draw.line(window, DARKGRAY, (col * CELLSIZE, 0), (col * CELLSIZE, WINDOWHEIGHT))
    # 绘制横线
    for row in range(1, CELLHEIGHT):  # 480
        pygame.draw.line(window, DARKGRAY, (0, row * CELLSIZE), (WINDOWWIDTH, row * CELLSIZE))


def draw_snake(snake_coords):
    """
    绘制蛇,即循环绘制列表中每一个坐标点
    :return:
    """
    for snake_coord in snake_coords:
        # 获取网格坐标（x:5-29, y:3-21）,需要将蛇头坐标倍增到界面坐标
        x = snake_coord[0] * CELLSIZE
        y = snake_coord[1] * CELLSIZE
        # 绘制矩形
        pygame.draw.rect(window, DARKGREEN, (x, y, CELLSIZE, CELLSIZE))
        # 绘制中心矩形
        pygame.draw.rect(window, GREEN, (x + 4, y + 4, CELLSIZE - 8, CELLSIZE - 8))


def show_splash_page():
    """
    显示首界面函数
    :return:
    """
    # 加载Snake文字，splash page 初始界面
    # 加载Press a key  to play 文字
    snakeSurface = bigFont.render('Snake', True, GREEN)
    # 矩形，得到矩形表面的左上角，右下角坐标，方便放置画面中心
    snakeRect = snakeSurface.get_rect()  # <rect(0, 0, 276, 129)>
    # 修改矩形中心，138 65 -- 320 240
    snakeRect.center = (int(WINDOWWIDTH / 2), int(WINDOWHEIGHT / 2))
    # 绘制背景色
    # 背景
    window.fill(BGCOLOR)
    # 展示snake，blit-传图
    window.blit(snakeSurface, snakeRect)
    # 显示提示
    show_tip()
    # 刷新，这个有什么用？这个步骤是用来刷新初始化的黑色界面，变成现在渲染的有字体的起始界面
    pygame.display.flip()
    # 循环界面
    while True:
        # 获取退出事件
        terminal()
        # 是否有键盘点击事件
        if pygame.event.get(KEYDOWN):  # pygame.locals.KEYDOWN
            # 如果列表不为空,说明有键盘点击事件,退出函数
            # 清空事件
            pygame.event.get()
            return
        # 清空事件
        pygame.event.get()


def random_snake_coordinate():
    # 随机头部
    headX = random.randint(5, CELLWIDTH - 3)
    headY = random.randint(3, CELLHEIGHT - 3)
    # 初始化贪吃蛇坐标(网格坐标)
    snakeCoords = [(headX, headY), (headX - 1, headY), (headX - 2, headY)]
    return snakeCoords


def random_apple_coordinate():
    x = random.randint(3, CELLWIDTH - 3)
    y = random.randint(3, CELLHEIGHT - 3)
    return x, y


def draw_apple(apple_coords):
    '''
    根据苹果的坐标绘制苹果
    :param appleCoord:苹果坐标
    :return:
    '''
    x = apple_coords[0] * CELLSIZE
    y = apple_coords[1] * CELLSIZE
    # 绘制矩形
    pygame.draw.rect(window, RED, (x, y, CELLSIZE, CELLSIZE))


def draw_score(apple_eaten):
    '''
    绘制分数
    :param score:
    :return:
    '''
    scoreSurface = smallFont.render('Score:{}'.format(apple_eaten), True, WHITE)
    # 显示
    window.blit(scoreSurface, (WINDOWWIDTH - 100, 20))


def show_game_page():
    """
    游戏界面函数
    :return:
    """
    # 默认贪吃蛇行走方向往右
    direction = Direction.RIGHT
    # 获得随机连续蛇身坐标，列表[(),]
    snakeCoords = random_snake_coordinate()
    # 获得随机苹果坐标，元组()
    appleCoord = random_apple_coordinate()
    # 设置分数
    score = 0
    # 循环界面
    while True:
        # 是否要退出
        terminal()

        # 获取点击事件，获取按键方向, 更新direction
        for event in pygame.event.get(KEYDOWN):
            if event.key == K_a and direction != Direction.RIGHT:
                direction = Direction.LEFT
            elif event.key == K_d and direction != Direction.LEFT:
                direction = Direction.RIGHT
            elif event.key == K_w and direction != Direction.DOWN:
                direction = Direction.UP
            elif event.key == K_s and direction != Direction.UP:
                direction = Direction.DOWN

        # 贪吃蛇根据方向行走
        # 原来的头，对蛇头进行处理，根据方向创建新的头
        oldHead = snakeCoords[0]
        newHead = None
        if direction == Direction.RIGHT:
            newHead = [oldHead[0] + 1, oldHead[1]]
        elif direction == Direction.LEFT:
            newHead = [oldHead[0] - 1, oldHead[1]]
        elif direction == Direction.UP:
            newHead = [oldHead[0], oldHead[1] - 1]
        elif direction == Direction.DOWN:
            newHead = [oldHead[0], oldHead[1] + 1]
        # 添加新的头
        snakeCoords.insert(0, newHead)

        # 碰撞检测，蛇头坐标是否与苹果坐标重合(为什么是oldHead)
        # 重合（吃掉苹果），1. 身体变长，2. 不需要删除尾巴，3. 分数增加
        # 不重合（没有吃掉苹果），1. 每移动一格删除尾巴
        if oldHead[0] == appleCoord[0] and oldHead[1] == appleCoord[1]:
            # 碰撞苹果+重新生成苹果+分数增加+不删除尾巴
            appleCoord = random_apple_coordinate()
            score += 1
        else:
            # 没有碰撞苹果+删除尾巴
            del snakeCoords[-1]  # -1 表示最后一个元素

        # 判断游戏是否结束，
        # 新头的越界检查
        if newHead[0] < 0 or newHead[0] > CELLWIDTH - 1 or newHead[1] < 0 or newHead[1] > CELLHEIGHT - 1:
            # 游戏结束
            return
        # 新头碰撞检测，逻辑，新头的xy与身体后的任意部分xy坐标相同
        for index in range(1, len(snakeCoords)):
            if newHead[0] == snakeCoords[index][0] and newHead[1] == snakeCoords[index][1]:
                # 身体碰撞
                return


        # 背景
        window.fill(BGCOLOR)
        # 绘制网格
        draw_grid()
        # 绘制贪吃蛇
        draw_snake(snakeCoords)
        # 绘制苹果
        draw_apple(appleCoord)
        # 绘制分数
        draw_score(len(snakeCoords) - 3)
        # 刷新
        pygame.display.flip()

        # 控制帧数
        clock.tick(4)



def show_game_over_page():
    """
    游戏结束界面函数
    :return:
    """
    # 设置结束界面显示的字体属性
    gameSurface = centerFont.render('Game', True, WHITE)  # Game字体贴图属性
    overSurface = centerFont.render('Over', True, WHITE)  # Over字体贴图属性
    # 获取这些字体的矩形特征，坐上+右下坐标
    gameRect = gameSurface.get_rect()
    overRect = overSurface.get_rect()
    # 将这些矩形的中间坐标midbotton/midtop设置成（x：窗口宽度的一半，y：窗口高度的一半+/-10）
    gameRect.midbottom = (int(WINDOWWIDTH / 2), int(WINDOWHEIGHT / 2 - 10))  # 向上偏移10
    overRect.midtop = (int(WINDOWWIDTH / 2), int(WINDOWHEIGHT / 2 + 10))  # 向下偏移10
    # 渲染窗口(窗口贴图)
    # blit(source, dest., area=None, special_flags=0) -> Rect
    # Draws a source Surface onto this Surface.
    window.blit(gameSurface, gameRect)
    window.blit(overSurface, overRect)
    # 显示提示
    show_tip()
    # 对初始化的窗口进行刷新, update the full display Surface to the screen
    pygame.display.flip()
    # 引擎，循环界面捕获事件，
    # 如果quit事件，退出游戏+程序，
    # 如果press事件，则继续获取事件，并跳出循环
    while True:
        # 获取退出事件（ESC）
        terminal()
        # 获取事件，任何按键点击退出当前界面，回到游戏界面
        if pygame.event.get(KEYDOWN):
            # 清空事件
            pygame.event.get()
            # 跳出当前循环
            return
        # 清空事件，继续捕获
        pygame.event.get()



"""------------------------- start game -------------------------"""
# 定义全局窗口
window = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
def start():
    """
    引擎函数
    :return:
    """
    global window, bigFont, centerFont, smallFont, clock
    # 初始化pygame
    pygame.init()
    # 创建窗口
    window = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    # 定义大文字
    bigFont = pygame.font.Font('resources/ARBERKLEY.ttf', 100)
    # 中号字体
    centerFont = pygame.font.Font('resources/ARBERKLEY.ttf', 50)
    # 定义小文字
    smallFont = pygame.font.Font('resources/ARBERKLEY.ttf', 18)
    # 创建Clock
    clock = pygame.time.Clock()
    # 显示首界面（done）
    show_splash_page()
    while True:  # 游戏引擎
        # 显示游戏界面
        show_game_page()
        # 显示游戏结束界面
        show_game_over_page()


"""------------------------- test area -------------------------"""
def test_init():
    global window, bigFont, centerFont, smallFont, clock
    # 初始化pygame
    pygame.init()
    # 创建窗口
    window = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    # 定义大文字
    bigFont = pygame.font.Font('resources/ARBERKLEY.ttf', 100)
    # 中号字体
    centerFont = pygame.font.Font('resources/ARBERKLEY.ttf', 50)
    # 定义小文字
    smallFont = pygame.font.Font('resources/ARBERKLEY.ttf', 18)
    # 创建Clock
    clock = pygame.time.Clock()


def test_show_splash_page():
    """
    测试初始化界面
    :return:
    """
    test_init()
    # 显示首界面（done）
    show_splash_page()


def test_show_game_page():
    """
    TODO: 测试游戏界面--主要功能界面
    :return:
    """
    test_init()
    # 显示首界面（done）
    show_game_page()


def test_show_game_over_page():
    """
    测试游戏结束界面
    :return:
    """
    test_init()
    show_game_over_page()


def test_draw_snake():
    test_init()
    headX = 9
    headY = 8
    snakeCoords = [(headX, headY), (headX - 1, headY), (headX - 2, headY)]
    draw_snake(snakeCoords)


def test_draw_grid():
    test_init()
    draw_grid()


def test_main():
    # test_show_splash_page()
    # test_show_game_page()
    # test_show_game_over_page()
    # test_draw_snake()
    test_draw_grid()


"""------------------------- main area -------------------------"""
if __name__ == '__main__':
    start()

    # test_main()
