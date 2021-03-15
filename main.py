from algorithms import selectionSort
import random
import time

# Set sorting speed 
speed = 0
def setSpeed():
    global speed
    selection = int(input("Enter a number from 1 to 3 (1 is slowest 3 is fastest): "))
    if selection == 3:
        speed = .05
    elif selection == 2:
        speed = .15
    else: 
        speed = .25
    #speed = float(input("Enter a number between 0 and 1: "))
    
# Test array
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]

# Randomise and print starting array
random.shuffle(arr)
print(arr)

# Call set speed function
setSpeed()
print(speed)
time.sleep(2)

# Call bubbleSort function
#bubbleSort(arr, speed)

# Call selection sort
selectionSort(arr, speed)

print ('Sorted array is:')
for i in range (len(arr)):
    print("%d" %arr[i]),