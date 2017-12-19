# Arman Ashrafian
# Sorting Algorithms

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
 
    # Keep popping from stack while is not empty
    while top >= 0:
 
        # Pop high and low
        high = stack[top]
        top = top - 1
        low = stack[top]
        top = top - 1
 
        # Set pivot element at its correct position in
        # sorted array
        p = part( arr, low, high )

        if(p == partition1): counter += 8
        else: counter += 10 
 
        # If there are elements on left side of pivot,
        # then push left side to stack
        if p-1 > low:
            top = top + 1
            stack[top] = low
            top = top + 1
            stack[top] = p - 1
 
        # If there are elements on right side of pivot,
        # then push right side to stack
        if p+1 < high:
            top = top + 1
            stack[top] = p + 1
            top = top + 1
            stack[top] = high

        counter += 16
    return counter

# picks first value for pivot
def partition1(arr, low, high):
    pivot = arr[low]
    border = low

    for i in range(low, high + 1):
        if arr[i] < pivot:
            border += 1
            arr[i], arr[border] = arr[border], arr[i]
    arr[low], arr[border] = arr[border], arr[low]
    
    return border

# picks middle value for pivot
def partition2(arr, low, high):
    mid = (high + low) // 2
    pivot = arr[mid]
    arr[mid], arr[low] = arr[low], arr[mid]
    border = low

    for i in range(low, high + 1):
        if arr[i] < pivot:
            border += 1
            arr[i], arr[border] = arr[border], arr[i]
    arr[low], arr[border] = arr[border], arr[low]
    
    return border   

# picks middle value for pivot
def partition3(arr, low, high):
    pivotIndex = random.randint(low, high)
    pivot = arr[pivotIndex]
    arr[pivotIndex], arr[low] = arr[low], arr[pivotIndex]
    border = low

    for i in range(low, high + 1):
        if arr[i] < pivot:
            border += 1
            arr[i], arr[border] = arr[border], arr[i]
    arr[low], arr[border] = arr[border], arr[low]
    
    return border 