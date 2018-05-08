# Find the only element in an array that only occurs once.

# big O(n)
def find_single_occurrence(array):
    hashTable = dict()
    # add all elements into hashtable
    for element in array:
        if element not in hashTable:
            hashTable[element] = 1
        else:
            hashTable[element] += 1
    # find element that only occurs once
    for key in hashTable.keys():
        if hashTable[key] is 1:
            return key


def test_find_single_occurrence():
    assert (find_single_occurrence([1, 2, 1, 2, 4, 5, 5, 8, 7, 8, 7]) == 4)
    assert (find_single_occurrence([3, 3, 3, 2, 1, 1, 1]) == 2)
