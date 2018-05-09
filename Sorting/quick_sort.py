#Implement quick sort
#from wikipiedia:
# The steps are:
#
# Pick an element, called a pivot, from the array.
# Partitioning: reorder the array so that all elements with values less than the pivot come before the pivot, while all elements with values greater than the pivot come after it (equal values can go either way). After this partitioning, the pivot is in its final position. This is called the partition operation.
# Recursively apply the above steps to the sub-array of elements with smaller values and separately to the sub-array of elements with greater values.
#
#helpful stackoverflow answer: https://stackoverflow.com/questions/18262306/quicksort-with-python
##
import random


def sort(array=[12, 4, 5, 6, 7, 3, 1, 15]):
    less = [] #left
    equal = [] #center
    greater = [] #right

    if len(array) > 1:
        pivot = array[random.randint(0, len(array) - 1)]  # pick a pivot point, it can be random
        for x in array:
            if x < pivot:  ## if less than the current pivot point add to less array, will be the left side
                less.append(x)
            if x == pivot:
                equal.append(x) #if equal add to equal area, this will be the center of the array
            if x > pivot:
                greater.append(x) ## if greater than the current pivot point add to greater array, will be the right side

        return sort(less) + equal + sort(greater) # join the arrays less on left greater on right of equal
    else:  # You need to hande the part at the end of the recursion - when you only have one element in your array, just return the array.
        return array


print sort([4, 10, 3, 8, 2, 9, 1])
