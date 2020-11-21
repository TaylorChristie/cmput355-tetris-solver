import pygame
import time
from copy import deepcopy
import math

# Based off of https://levelup.gitconnected.com/tetris-ai-in-python-bd194d6326ae


class Event():
    type = None
    key = None

    def __init__(self, type, key):
        self.type = type
        self.key = key


# Taken from tetris.py, exact same code
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
                try:
                    simulated[i + y][j + x] = 1
                except IndexError:
                    return None
    return simulated

counter = 0
VECTORS = {
    'cleared': 5,
    'holes': -5,
    'max_height': -3,
    'roughness': -0.5
}


def run(field, figure, width, height):
    global counter
    global VECTORS
    counter += 1
    if counter < 3:
        return []
    counter = 0

    best = None
    for i in range(len(figure.figures[figure.type])):
        figure.rotate()
        for x in range(width+1):
            y = 0
            while not calculate_intersection(field, x, y, height, width, figure.image()):
                y += 1
            y -= 1
            simulated = simulate_placement(field, figure, x, y)

            if simulated:

                # calculate roughness (sum of height differences between adjacent columns)
                heights = []
                for c in range(len(simulated[0])):
                    for r in range(len(simulated)):
                        if simulated[r][c]:
                            heights.append(len(field)-r)
                            break
                holes = 0
                for c in range(len(simulated[0])):
                    initial = False
                    for r in range(len(simulated)):
                        if simulated[r][c]:
                            initial = True
                        elif initial:
                            holes += 1
                cleared = 0
                max_height = max(heights)
                
                roughness = 0
                for a in range(len(heights)):
                    if a > 0:
                        roughness += abs(heights[a-1] - heights[a])
                    if a < len(heights) - 1:
                        roughness += abs(heights[a+1] - heights[a])
                for r in simulated:
                    if all(r):
                        cleared += 1

            # max height of the board?
            score = VECTORS['holes'] * holes + VECTORS['max_height'] * max_height + VECTORS['cleared'] * cleared + VECTORS['roughness'] * roughness

            if simulated and (best == None or score > best[5]):
                best = [x, i, y, simulated, holes, score, cleared, max_height, roughness, heights]

    figure.rotate()
    off = best[0]
    rotates = best[1]
    print('proposed placement|x='+str(off)+'|rotates='+str(best[1])+'|holes='+str(
        best[4])+'|cleared='+str(best[6])+'|max_height='+str(best[7])+'|roughness='+str(best[8])+'|heights='+str(best[9])+'|score='+str(best[5]))
    # time.sleep(0.1)

    # translates offset and rotates into in game moves for feedback
    events = [Event(pygame.KEYDOWN, pygame.K_UP) for x in range(rotates)]
    if off == 0:
        events = events + [Event(pygame.KEYDOWN, pygame.K_LEFT)
                           for x in range(10)]
    else:
        events = events + [Event(pygame.KEYDOWN, pygame.K_RIGHT)
                           for x in range(off)]
    events.append(Event(pygame.KEYDOWN, pygame.K_SPACE))
    return events
