import math
import pygame
from random import randint
import time

pygame.init()
size = (500, 500)
window = pygame.display.set_mode((size))
pygame.display.set_caption("Introsort")
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)

ourlist = []
listLength = 100
xList, y, w = [], 0, 5
tmpX = 0
for i in range(listLength):
    ourlist.append(randint(0, 500))
    #ourlist.append(i+100)
    xList.append(tmpX)
    tmpX += w


def draw():
    global xList, y, ourlist
    for i in range(listLength):
        pygame.draw.rect(window, white, (xList[i], y, w, ourlist[i]), 0)

def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and arr[i] < arr[l]:
        largest = l
    if r < n and arr[largest] < arr[r]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap
        heapify(arr, n, largest)


def heapSort(arr):
    n = len(arr)
    for i in range(n, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
        time.sleep(.1)
        window.fill(black)
        draw()
        pygame.display.update()

def partition(arr, low, high):
    i = (low - 1)
    pivot = arr[high]

    for j in range(low, high):

        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)

def introSort(sortablelist):
    maxdepth = int(math.floor(math.log(len(sortablelist)))) * 2
    introHelp(sortablelist, maxdepth, 0, len(sortablelist)-1)

def introHelp(sortablelist, maxdepth, first, last):
    n = len(sortablelist)
    if n <= 1:
        pass
    elif maxdepth == 0:
        heapSort(sortablelist)
    else:
        middle = partition(sortablelist, first, last)
        introHelp(sortablelist, maxdepth - 1, first, middle - 1)
        introHelp(sortablelist, maxdepth - 1, middle + 1, last)

introSort(ourlist)

for event in pygame.event.get():
    if event.type == pygame.QUIT:
        pygame.quit()