import math
import random
from random import randint
import time


def partition(arr, low, high):
    i = (low - 1)
    pivot = arr[high]

    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quickSort(arr, low, high):
    if len(arr) == 0:
        pass
    elif low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)


def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and arr[i] < arr[l]:
        largest = l
    if r < n and arr[largest] < arr[r]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heapSort(arr):
    for i in range(len(arr), -1, -1):
        heapify(arr, len(arr), i)
    for i in range(len(arr) - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)


def introsort(arr, maxdepth, low, high):
    if maxdepth == 0:
        heapSort(arr)
    if low < high:
        pi = partition(arr, low, high)
        introsort(arr,maxdepth - 1, low, pi - 1)
        introsort(arr,maxdepth - 1, pi + 1, high)


if __name__ == '__main__':
    arr = []
    arr2 = []
    listLength = 1000
    for i in range(listLength):
        arr.append(randint(0, 500))
        arr2.append(randint(0, 500))
    timeoutstart = time.time()

    quickSort(arr, 0, listLength-1)
    timeoutend = time.time()
    end = timeoutend - timeoutstart
    print('quicksort: ' + str(end))

    timeoutstart = time.time()
    #heapSort(arr)
    timeoutend = time.time()
    end = timeoutend - timeoutstart
    #print('heapsort: ' + str(end))

    maxdepth = int(math.floor(math.log(len(arr2)))) * 2

    timeoutstart = time.time()
    introsort(arr2, maxdepth, 0, 99)
    timeoutend = time.time()
    end = timeoutend - timeoutstart
    print('introsort: ' + str(end))