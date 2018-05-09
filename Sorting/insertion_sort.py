# Implement insertion sort
# Big O(n^2)
def insertion_sort(array):
    for i in range(len(array)):
        j = i
        while j > 0 and array[j - 1] > array[j]:
            # swap array[j-1]> array[j]
            array = swap(array, j - 1, j)
            j -= 1
    return array


def swap(array, a, b):
    swapA = array[a]
    swapB = array[b]
    array[a] = swapB
    array[b] = swapA
    return array


def test_insertion_sort():
    assert (insertion_sort([3, 2, 4, 1]) == [1, 2, 3, 4])
