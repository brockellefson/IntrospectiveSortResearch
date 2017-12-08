
import pygame
from random import randint
import winsound
import time

pygame.init()
size = (500, 500)
window = pygame.display.set_mode((size))
pygame.display.set_caption("Quicksort")
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)

ourlist = []
listLength = 100
xList, y, w = [], 0, 5
tmpX = 0
for i in range(listLength):
    #ourlist.append(randint(0, 500))
    ourlist.append(i+100)
    xList.append(tmpX)
    tmpX += w

def draw():
    global xList, y, ourlist
    for i in range(listLength):
        pygame.draw.rect(window, white, (xList[i], y, w, ourlist[i]), 0)

def partition(arr, low, high):
    i = (low - 1)
    pivot = arr[high]

    for j in range(low, high):

        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)


def quickSort(arr, low, high):
    if low < high:
        time.sleep(.1)
        window.fill(black)
        draw()
        pygame.display.update()
        winsound.Beep(1000, 5)
        pi = partition(arr, low, high)
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)

quickSort(ourlist, 0, listLength-1)

for event in pygame.event.get():
    if event.type == pygame.QUIT:
        pygame.quit()