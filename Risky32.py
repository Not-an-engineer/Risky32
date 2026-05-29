import os
import sys
import time
import random
import pygame
from pygame.locals import *
import numpy as np
import win32api
import win32con
import win32gui



pygame.init()
window_size = pygame.display.get_desktop_sizes()[0]
window = pygame.display.set_mode(window_size, pygame.FULLSCREEN | pygame.NOFRAME)

fuchasia = (255, 0, 128)

# Create layered window
hwnd = pygame.display.get_wm_info()["window"]
win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE, win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE) | win32con.WS_EX_LAYERED)
# Set window transparency color
win32gui.SetLayeredWindowAttributes(hwnd, win32api.RGB(*fuchasia), 0, win32con.LWA_COLORKEY)


class Snake:
    def __init__(self):
        self.body = [(window_size[0] // 2, window_size[1] // 2)]
        self.direction = (0, -10)  # Initial direction: up
    
    def move(self):
        head_x, head_y = self.body[0]
        dir_x, dir_y = self.direction
        new_head = (head_x + dir_x, head_y + dir_y)
        self.body.insert(0, new_head)  # Add new head
        self.body.pop()  # Remove tail
    
    def display(self, surface):
        for segment in self.body:
            pygame.draw.rect(surface, (0, 255, 0), (*segment, 10, 10))  # Draw snake segments
    
    def change_direction(self, new_direction):
        # Prevent the snake from reversing
        if (new_direction[0] * -1, new_direction[1] * -1) != self.direction:
            self.direction = new_direction


snake = Snake()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:  # noqa: F405
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
    window.fill(fuchasia)
    snake.move()
    snake.display(window)
    time.sleep(1)  # Control the speed of the snake
    
    pygame.display.update()


# TODO: Make snake move with arrow keys or WASD keys
# TODO: Make the snake itself the size of files (10x10 pixels for example)


# TODO: Make snake trail
# TODO: Make apples spawn randomly
# TODO: Make snake grow when it eats an apple
# TODO: Make apple a copy of a file from a custom folder (Just to test at first, so that we dont use real sys32 files)
# TODO: Make file delete when snake eats "apple" (Just to test at first, so that we dont use real sys32 files)