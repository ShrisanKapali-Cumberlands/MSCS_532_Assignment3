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


## Implementing hash table using chaining to avoid collision
# Defining a hash table class that has insert, search, and delete methods
# Let us consider a class of products that has name as key and quanity as value
# Universal Hasing using modular arithmentic
# h(k)=((a⋅k+b)modp)modm => k=key, m=size
class HashTable:
    # Defining contructors
    def __init__(self, size, primeNumber):
        # Size is the number of has buckets
        self.size = size
        # Set the prime number
        self.prime = primeNumber
        # Get a and b value using random
        self.a = random.randint(1, primeNumber - 1)
        self.b = random.randint(0, primeNumber - 1)

        # Iniializing a list of {size} empty lists
        self.__table = [[] for _ in range(self.size)]

    # A hash function to map key to values
    def hash_function(self, key):
        prime = 31
        # simple rolling hash function using
        key_int = sum(ord(c) * prime**i for i, c in enumerate(str(key))) % self.size

        return ((self.a * key_int) % self.prime) % self.size

    # a function to insert record
    def insert_product(self, key, value):
        index = self.hash_function(key)
        for pair in self.__table[index]:
            if pair[0] == key:
                pair[1] = value  # Update existing key
                return
        self.__table[index].append([key, value])

    # a function to search product using key
    def search_product(self, key):
        index = self.hash_function(key)
        for pair in self.__table[index]:
            if pair[0] == key:
                return pair[1]

        # If the key is not found
        return None

    # a function to delete product using key
    def delete_product(self, key):
        index = self.hash_function(key)

        # If key is not in has table return
        for i, pair in enumerate(self.__table[index]):
            if pair[0] == key:
                del self.__table[index][i]
                return True
        # If Key not found
        return False


# Now the hash table has been created, running test cases
# Initializing hashtable of bucket size 10, and prime number 10000019 for reducing collision
hash_table = HashTable(10, 10000019)

# Inserting records in hash table
print("")
print("***************************************")
print("Initializing HashTable")
print("***************************************")
startTime = time.time()
hash_table.insert_product("calculator", 250.00)
endTime = time.time()
print(f"Execution time of inserting a calculator: {endTime - startTime:.6f} seconds")

startTime = time.time()
hash_table.insert_product("bottle", 35.00)
endTime = time.time()
print(f"Execution time of inserting a bottle: {endTime - startTime:.6f} seconds")

hash_table.insert_product("pen", 2.50)
hash_table.insert_product("earphone", 125.00)
hash_table.insert_product("headphone", 299.00)

# Searching for records in hash table
print("")
print("Searching value calculator in the HashTable")
startTime = time.time()
value = hash_table.search_product("calculator")
endTime = time.time()
print(
    "Value of key calculator = "
    + str(value)
    + f". The search time took {endTime - startTime:.6f} seconds"
)


# Deleting  records in hash table
print("Deleting calculator in a HashTable")
startTime = time.time()
hash_table.delete_product("calculator")
endTime = time.time()
print(f"Time taken to delete calculator: {endTime - startTime:.6f} seconds")
print(
    "Searching for the value of calculator after deletion: ",
    hash_table.search_product("calculator"),
)
