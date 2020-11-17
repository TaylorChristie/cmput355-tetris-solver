import pygame
import time
from copy import deepcopy

# Based off of https://levelup.gitconnected.com/tetris-ai-in-python-bd194d6326ae

class Event():
    type = None
    key = None

    def __init__(self, type, key):
        self.type = type
        self.key = key


## Taken from tetris.py, exact same code
def calculate_intersection(field, x, y, height, width, image):
    intersection = False
    for i in range(4):
        for j in range(4):
            if i * 4 + j in image:
                if i + y > height - 1 or \
                        j + x > width - 1 or \
                        j + x < 0 or \
                        field[i + y][j + x] > 0:
                    intersection = True
    return intersection


def simulate_placement(field, figure, x, y):
    simulated = deepcopy(field)
    for i in range(4):
        for j in range(4):
            if i * 4 + j in figure.image():
                simulated[i + y][j + x] = 1
    return simulated

# TODO not working for 3,5,6,7
def calculate_figure_width(figure):
    # 0  1  2  3
    # 4  5  6  7
    # 8  9  10 11
    # 12 13 14 15
    width = 0
    for i in range(4):
        r_width = 0
        for j in range(4):
            if i * 4 + j in figure.image():
                r_width += 1
        if r_width > width:
            width = r_width

    return width

counter = 0
def run(field, figure, width, height):
    global counter
    counter += 1
    if counter < 3:
        return []
    counter = 0
    
    best = None
    for i in range(len(figure.figures[figure.type])):
        figure.rotate()
        # TODO calculate width of the image
        offset = calculate_figure_width(figure)
        print('image:',figure.image())
        print('width:', offset)
        for x in range(width-offset):
            y = 0
            while not calculate_intersection(field, x, y, height, width, figure.image()):
                y += 1
            y -= 1
            simulated = simulate_placement(field, figure, x, y)
            print('proposed placement|x='+str(x)+',y='+str(y))
            [print(r) for r in simulated]
            if best == None or y > best[2]:
                best = [x, i, y]
    
    figure.rotation = 0
    off = best[0]
    rotates = best[1]
    events = [Event(pygame.KEYDOWN, pygame.K_UP) for x in range(rotates)]
    if off == 0:
        events = events + [Event(pygame.KEYDOWN, pygame.K_LEFT) for x in range(10)]
    else:
        events = events + [Event(pygame.KEYDOWN, pygame.K_RIGHT) for x in range(off)]
    events.append(Event(pygame.KEYDOWN, pygame.K_SPACE))
    return events