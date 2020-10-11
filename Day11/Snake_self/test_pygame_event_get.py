import pygame
from pygame.locals import *


def terminal():
    pass


def test_event_get_0():
    while True:
        for event in pygame.event.get(KEYDOWN):
            print(event)


def test_event_get_1():
    while True:
        event_list = pygame.event.get()
        print(event_list)


if __name__ == '__main__':
    window = pygame.display.set_mode((640, 480))

    pygame.init()

    # test_event_get_0()
    test_event_get_1()
