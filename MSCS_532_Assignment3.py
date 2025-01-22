# MSCS 532 Algorithm and Data Structure
# Assignment 3
# Shrisan Kapali
# Student Id : 005032249

# Randomized Quick Sort Analysis
# Implementation of partion method for randomized quick sort
# Importing random & time library
import random
import time
import sys

# Increase the system recursion to 500000
sys.setrecursionlimit(500000)


# Creating a method that implements randomized partition
def randomized_partition(array, low, high):
    # Using random pick a number between low, high
    pivotIndex = random.randint(low, high)
    # Swapping array at pivot with last element
    array[pivotIndex], array[high] = array[high], array[pivotIndex]
    # Select pivot as array at higher position
    pivot = array[high]
    # Starting pointer i at low-1 position
    i = low - 1

    # Loop pointer j from low to high
    for j in range(low, high):
        # For j is array at position j is less than pivot, swap
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]

    # Swap array at position i+1 with high
    array[i + 1], array[high] = array[high], array[i + 1]

    return i + 1


# Implementation of Quick Sort
def randomized_quicksort(array, low, high):
    if low < high:
        pivot = randomized_partition(array, low, high)
        # Left side partition
        randomized_quicksort(array, low, pivot - 1)
        # Right side partition
        randomized_quicksort(array, pivot + 1, high)


# Test cases
emptyArray = []
sortedArray = list(range(0, 500000))
reverseSortedArray = list(range(500000, 0, -1))
randomSortedArray = [random.randint(1, 5000) for _ in range(500000)]

# Running quick sort and calculating execution time
startTime = time.time()
randomized_quicksort(emptyArray, 0, len(emptyArray) - 1)
endTime = time.time()
print("Running randomized quick sort on empty")
print(f"Execution time: {endTime - startTime:.6f} seconds")

startTime = time.time()
randomized_quicksort(sortedArray, 0, len(sortedArray) - 1)
endTime = time.time()
print("")
print("Running randomized quick sort on sorted array of size 500000")
print(f"Execution time: {endTime - startTime:.6f} seconds")

startTime = time.time()
randomized_quicksort(reverseSortedArray, 0, len(reverseSortedArray) - 1)
endTime = time.time()
print("")
print("Running randomized quick sort on reverse sorted array of size 500000")
print(f"Execution time: {endTime - startTime:.6f} seconds")


startTime = time.time()
randomized_quicksort(randomSortedArray, 0, len(randomSortedArray) - 1)
endTime = time.time()
print("")
print("Running randomized quick sort on random sorted array of size 500000")
print(f"Execution time: {endTime - startTime:.6f} seconds")


## Implementation of Deterministic Quick sort using first element as pivot
def deterministic_partition(array, low, high):
    # Using the first element as pivot
    pivot = array[low]
    i = low + 1
    j = high

    while True:
        # For pointer i find the element at i that is greater than pivot
        while i <= j and array[i] <= pivot:
            i += 1
        # For pointer i find the element at j that is less than pivot
        while i <= j and array[j] > pivot:
            j -= 1
        # Swap i,j
        if i <= j:
            array[i], array[j] = array[j], array[i]
        else:
            break

    array[low], array[j] = array[j], array[low]
    return j


def deterministic_quicksort(array, low, high):
    if low < high:
        pivot = deterministic_partition(array, low, high)
        deterministic_quicksort(array, low, pivot - 1)
        deterministic_quicksort(array, pivot + 1, high)


# Test cases
emptyArray = []
sortedArray = list(range(0, 20000))
reverseSortedArray = list(range(20000, 0, -1))
randomSortedArray = [random.randint(1, 5000) for _ in range(500000)]

# Running quick sort and calculating execution time
startTime = time.time()
deterministic_quicksort(emptyArray, 0, len(emptyArray) - 1)
endTime = time.time()
print("Running deterministic quick sort on empty")
print(f"Execution time: {endTime - startTime:.6f} seconds")

startTime = time.time()
deterministic_quicksort(sortedArray, 0, len(sortedArray) - 1)
endTime = time.time()
print("")
print("Running deterministic quick sort on sorted array of size 20000")
print(f"Execution time: {endTime - startTime:.6f} seconds")

startTime = time.time()
deterministic_quicksort(reverseSortedArray, 0, len(reverseSortedArray) - 1)
endTime = time.time()
print("")
print("Running deterministic quick sort on reverse sorted array of size 20000")
print(f"Execution time: {endTime - startTime:.6f} seconds")


startTime = time.time()
deterministic_quicksort(randomSortedArray, 0, len(randomSortedArray) - 1)
endTime = time.time()
print("")
print("Running deterministic quick sort on random sorted array of size 500000")
print(f"Execution time: {endTime - startTime:.6f} seconds")
