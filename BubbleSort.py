
import pygame
from random import randint
import time

pygame.init()
size = (500, 500)
window = pygame.display.set_mode((size))
pygame.display.set_caption("BubbleSort")
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)

ourlist = []
listLength = 100
xList, y, w = [], 0, 5
tmpX = 0
for i in range(listLength):
    ourlist.append(randint(0, 500))
    xList.append(tmpX)
    tmpX += w


def draw():
    global xList, y, ourlist
    for i in range(listLength):
        pygame.draw.rect(window, white, (xList[i], y, w, ourlist[i]), 0)



for i in range(listLength):
    for j in range(0, listLength - i - 1):

        if ourlist[j] > ourlist[j + 1]:
            ourlist[j], ourlist[j + 1] = ourlist[j + 1], ourlist[j]
            window.fill(black)
            draw()
            pygame.display.update()
            time.sleep(.1)

for event in pygame.event.get():
    if event.type == pygame.QUIT:
        pygame.quit()