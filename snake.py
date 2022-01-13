from pygame import *
import pygame
from pygame.locals import *
import random

pygame.init()

screen = pygame.display.set_mode((800, 600))


# create a background class
class snake_head:
    def __init__(self):
        self.head = pygame.image.load("snake.png")


# make a snake head class of a pic of a snake
class background:
    def __init__(self):
        self.surface = pygame.Surface((800, 600))
        self.surface.fill((170, 170, 170))


# make a snake body class with a pic of square
class snake_body:
    def __init__(self):
        self.body = pygame.image.load("square.png")


bg = background()
player = snake_head()
body = snake_body()

x = 400
y = 300
bx = x
by = y + 32

cx = 0
cy = -0.1
cbx = 0
cby = -0.1


def blit_player():
    global x, y
    screen.blit(bg.surface, (0, 0))
    screen.blit(player.head, (x, y))


def blit_body():
    global cx, cy, x, y, bx, by, cby
    cbx = 0
    cby = 0
    #TODO: goes up in the beginning
    if cy == -0.1 and bx == x :
        by += cy

        screen.blit(body.body, (bx, by))

    # TODO: turns right or left from up
    if cx == 0.1 and by > y and x > bx:
        #print("hamza")
        by -= cx
        screen.blit(body.body, (bx, by))

    # TODO: turns  left from up
    if cx == -0.1 and by > y and x < bx:
        by += cx
        screen.blit(body.body, (bx, by))
    # TODO: keeps going right
    if cx == 0.1 and int(by) == int(y):
        print("hamza")
        bx += cx
        screen.blit(body.body, (bx, by))

    # TODO: keeps going left
    if cx == -0.1 and int(by) == int(y):
        bx += cx
        screen.blit(body.body, (bx, by))

    #TODO: keeps going down from right and left
    if cy == 0.1 and int(bx) == int(x):
        by += cy
        screen.blit(body.body, (bx, by))




    #TODO: turns up or down from right
    if cy != 0 and bx < x:
        by += 0
        cbx = 0.1
        bx += cbx
        screen.blit(body.body, (bx, by))

    #TODO: turns up or down from left
    if cy != 0 and bx > x:
        by += 0
        cbx = -0.1
        bx += cbx
        screen.blit(body.body, (bx, by))



    #TODO: turns right or left from down
    if cx != 0 and cy == 0 and by < y:
        cby = -0.1
        by -= cby
        screen.blit(body.body, (bx, by))

def update_x_y():
    global x, y, cx, cy, bx, by, cbx, cby
    x += cx
    y += cy


run = True
px = 0
py = 0
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                run = False
            if event.key == K_RIGHT:
                if cx == -0.1:
                    break
                cx = 0.1
                cy = 0
            if event.key == K_LEFT:
                if cx == 0.1:
                    break
                cx = -0.1
                cy = 0
            if event.key == K_UP:
                if cy == 0.1:
                    break
                cy = -0.1
                cx = 0
            if event.key == K_DOWN:
                if cy == -0.1:
                    break
                cy = 0.1
                cx = 0

    if x > 800:
        x = 0
    if x < 0:
        x = 800
    if y < 0:
        y = 600 - 32
    if y > 600 - 32:
        y = 0
    update_x_y()
    blit_player()
    blit_body()
    pygame.display.flip()
