#File for sorting algorithms
import time


def renderArray(arr):
    for i in range (len(arr)):
        print("%d" %arr[i]),

# Bubble Sort
def bubbleSort(arr, speed):
    n = len(arr)

    #Traverse through all array elements
    for i in range(n-1):
    # range(n) also work but outer loop will repeat one more time than needed

        # last i elements are already in place
        for j in range (0, n-i-1):

            # traverse the array from 0 to n-i-1
            #swap if the element found is greater than the next element
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
                renderArray(arr)
                time.sleep(speed)

# Selection sort
def selectionSort(arr, speed):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        renderArray(arr)
        time.sleep(speed)


