#File for sorting algorithms
import time
import random 
# Bubble Sort
def bubbleSort(arr):
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
                print(arr)
                time.sleep(.1)

# Test array
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]

random.shuffle(arr)
print(arr)
time.sleep(2)
bubbleSort(arr)

print ('Sorted array is:')
for i in range (len(arr)):
    print("%d" %arr[i]),