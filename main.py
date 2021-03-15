from algorithms import bubbleSort
import random
import time

speed = 0

def setSpeed():
    global speed
    speed = float(input("Enter a number between 0 and 1: "))
    



#speed = float(input("Enter a number between 0 and 1: "))


print(speed)
# Test array
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]

random.shuffle(arr)
print(arr)
setSpeed()
print(speed)
time.sleep(2)
bubbleSort(arr, speed)

print ('Sorted array is:')
for i in range (len(arr)):
    print("%d" %arr[i]),