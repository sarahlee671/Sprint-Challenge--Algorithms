#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n) Based on the size of the input data, it increases the running time


b) O(n^2) For each value, it needs to compare to all other values in the list.


c) O(n) (Linear Time) It runs recursively with one call each time until it is 0

## Exercise II


# Binary search
#Find the middle floor and drop egg
#If the egg breaks, go to the left array and drop egg and repeat until it doesn't break
#If it doesn't break, go to the right array and drop egg and repeat until it does break
# Time Complexity is O(log n)

def egg_break(floors):
    current_floor = 0
    if len(floors) > 1:
        middle_floor = len(floor)//2
        if floors[middle_floor] == 1:
            current_floor = middle_floor
            left_floors = egg_breaks(floors[ :middle_floor -1])
        else:
            right_floors = egg_breaks(floors[middle_floor:  +1])
    return current_floor