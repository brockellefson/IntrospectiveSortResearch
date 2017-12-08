import pygame
from random import randint
import time

pygame.init()
size = (500, 500)
window = pygame.display.set_mode((size))
pygame.display.set_caption("Heapsort")
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)

ourlist = []
listLength = 100
xList, y, w = [], 0, 5
tmpX = 0
for i in range(listLength):
    ourlist.append(randint(0, 500))
    #ourlist.append(i+200)
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

heapSort(ourlist)

for event in pygame.event.get():
    if event.type == pygame.QUIT:
        pygame.quit()