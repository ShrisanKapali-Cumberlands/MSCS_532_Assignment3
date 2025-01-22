# MSCS 532 Algorithm and Data Structure
# Assignment 3
# Shrisan Kapali
# Student Id : 005032249

# Randomized Quick Sort Analysis
# Implementation of partion method for randomized quick sort
# Importing random & time library
import random
import time


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
print("Running quick sort on empty")
print(f"Execution time: {endTime - startTime:.6f} seconds")

startTime = time.time()
randomized_quicksort(sortedArray, 0, len(sortedArray) - 1)
endTime = time.time()
print("")
print("Running quick sort on sorted array of size 500000")
print(f"Execution time: {endTime - startTime:.6f} seconds")

startTime = time.time()
randomized_quicksort(reverseSortedArray, 0, len(reverseSortedArray) - 1)
endTime = time.time()
print("")
print("Running quick sort on reverse sorted array of size 500000")
print(f"Execution time: {endTime - startTime:.6f} seconds")


startTime = time.time()
randomized_quicksort(randomSortedArray, 0, len(randomSortedArray) - 1)
endTime = time.time()
print("")
print("Running quick sort on random sorted array of size 500000")
print(f"Execution time: {endTime - startTime:.6f} seconds")
