import sys
import pygame

from pygame.locals import *

from local import *



def terminal():
    """
    定义终止函数，退出pygame，退出程序
    :return:
    """
    pygame.quit()  # 退出pygame
    sys.exit()


def show_splash_page():
    """
    首界面显示，不停循环
    :return:
    """
    # 加载snake文字
    snake_surface = bigFont.render('Snake', True, GREEN)
    # 获取矩形
    snake_rect = snake_surface.get_rect()
    print(snake_rect)  # <rect(0, 0, 276, 129)> 左上角的坐标为 0，0
    # 背景界面
    window.fill(BGCOLOR)
    # 展示snake, blit 传图
    window.blit(snake_surface, (100, 100))  # 表示左上角的坐标
    # 刷新界面
    pygame.display.flip()
    while True:
        # get events from the queue，获取事件列表(获取事件的两种写法)
        # event_list = pygame.event.get()
        # for event in event_list:
        #     if event.type == QUIT:  # pygame.locals
        #         terminal()
        # 获取退出事件（第二种写法）
        event = pygame.event.get(QUIT)
        if event:
            terminal()


window = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
def start():
    # 全局变量区, 但是必须首先调用此函数，首界面窗口可以不用刷新显示，global表示可以修改
    global window, bigFont, smallFont
    # 初始化pygame
    pygame.init()
    # 创建窗口，This function will create a display Surface.
    window = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    # 定义大文字
    bigFont = pygame.font.Font('resources/ARBERKLEY.ttf', 100)
    # 中号字体
    centerFont = pygame.font.Font('resources/ARBERKLEY.ttf', 50)
    # 定义小文字
    smallFont = pygame.font.Font('resources/ARBERKLEY.ttf', 18)
    # 定义小的文字
    # 游戏引擎，显示首界面
    show_splash_page()
    # 显示游戏界面
    # 显示游戏结束界面


if __name__ == '__main__':
    start()
