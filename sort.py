# Arman Ashrafian
# Sorting Algorithms

# This file implements the following sorts:
# - quick sort
# - merge sort
# - heap sort
# - radix sort (strings)

import random

# Function to do Quick sort
# arr[] --> Array to be sorted,
# low   --> Starting index,
# high  --> Ending index
# part()--> Partition function
def quick_sort(arr, low, high, part):
    counter = 0

    # Create an auxiliary stack
    size = high - low + 1
    stack = [0] * (size)
 
    # initialize top of stack
    top = -1
 
    # push initial values of low and high to stack
    top = top + 1
    stack[top] = low
    top = top + 1
    stack[top] = high

    counter += 7
 
    # Keep popping from stack while is not empty
    while top >= 0:
 
        # Pop high and low
        high = stack[top]
        top = top - 1
        low = stack[top]
        top = top - 1

        counter += 4
 
        # Set pivot element at its correct position in
        # sorted array
        p, c = part( arr, low, high )
        counter += c
 
        # If there are elements on left side of pivot,
        # then push left side to stack
        if p-1 > low:
            top = top + 1
            stack[top] = low
            top = top + 1
            stack[top] = p - 1
            counter += 4
 
        # If there are elements on right side of pivot,
        # then push right side to stack
        if p+1 < high:
            top = top + 1
            stack[top] = p + 1
            top = top + 1
            stack[top] = high
            counter += 4

    return counter

# picks first value for pivot
def partition1(arr, low, high):
    counter = 0
    pivot = arr[low]
    border = low
    counter += 2
    for i in range(low, high + 1):
        counter += 1
        if arr[i] < pivot:
            border += 1
            arr[i], arr[border] = arr[border], arr[i]
            counter += 2

    arr[low], arr[border] = arr[border], arr[low]
    counter += 1
    
    return (border, counter)

# picks middle value for pivot
def partition2(arr, low, high):
    counter = 0
    mid = (high + low) // 2
    pivot = arr[mid]
    arr[mid], arr[low] = arr[low], arr[mid]
    border = low
    counter += 4

    for i in range(low, high + 1):
        counter += 1
        if arr[i] < pivot:
            border += 1
            arr[i], arr[border] = arr[border], arr[i]
            counter += 2
    arr[low], arr[border] = arr[border], arr[low]
    counter += 1

    return (border, counter)   

# picks middle value for pivot
def partition3(arr, low, high):
    counter = 0
    pivotIndex = random.randint(low, high)
    pivot = arr[pivotIndex]
    arr[pivotIndex], arr[low] = arr[low], arr[pivotIndex]
    border = low
    counter += 4

    for i in range(low, high + 1):
        counter += 1
        if arr[i] < pivot:
            border += 1
            arr[i], arr[border] = arr[border], arr[i]
            counter += 2
    arr[low], arr[border] = arr[border], arr[low]
    counter += 1

    return (border, counter)   

# sorts arr in place
# returns number of statements executed
def merge_sort(arr):
    if len(arr) <= 1: return 1

    counter = 0

    mid = len(arr)//2
    lefthalf = arr[:mid]
    righthalf = arr[mid:]

    counter += 3

    counter += merge_sort(lefthalf)
    counter += merge_sort(righthalf)

    i=0
    j=0
    k=0
    while i < len(lefthalf) and j < len(righthalf):
        if lefthalf[i] < righthalf[j]:
            arr[k]=lefthalf[i]
            i=i+1
        else:
            arr[k]=righthalf[j]
            j=j+1
        k=k+1
        counter += 8

    while i < len(lefthalf):
        arr[k]=lefthalf[i]
        i=i+1
        k=k+1
        counter += 4

    while j < len(righthalf):
        arr[k]=righthalf[j]
        j=j+1
        k=k+1
        counter += 4

    return counter

# To heapify subtree rooted at index i.
# returns statements executed
def heapify(arr, n, i):
    counter = 0

    largest = i  
    l = 2 * i + 1     
    r = 2 * i + 2     
    counter += 3

    if l < n and arr[i] < arr[l]:
        counter += 2
        largest = l

    if r < n and arr[largest] < arr[r]:
        counter += 2
        largest = r
 
    # Change root, if needed
    if largest != i:
        counter += 2
        arr[i],arr[largest] = arr[largest],arr[i]  # swap
 
        counter += heapify(arr, n, largest)
    return counter
 
# sorts arr in place
# returns statements executed
def heap_sort(arr):
    counter = 0
    n = len(arr)
    counter+=1
 
    # Build a maxheap.
    for i in range(n, -1, -1):
        counter += heapify(arr, n, i)
 
    # One by one extract elements
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]   # swap
        counter+=1
        counter += heapify(arr, i, 0)

    return counter

def radix_sort_string(arr, i):
    # base case
    if len(arr) <= 1:
        return arr 

    # divide by length then lex order
    done_bucket = []
    buckets = [ [] for x in range(27) ] # one bucket for each letter

    for s in arr:
        if i >= len(s):
            done_bucket.append(s)
        else:
            buckets[ ord(s[i]) - ord('a') ].append(s)
            
    for x in (done_bucket + [ b for blist in buckets for b in blist ]):
        print(x)

    print("\n")
    # recursively sort buckets
    buckets = [ radix_sort_string(b, i + 1) for b in buckets ]

    # chain all buckets together
    return done_bucket + [ b for blist in buckets for b in blist ]
