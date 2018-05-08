# Find the common elements of 2 int arrays

def find_common(array1, array2):
    hashTable = dict()
    sharedElements = set()
    # add all elements into hashtable, maybe better to use a set should have same time complexity though
    for element in array1:
        if element not in hashTable:
            hashTable[element] = True

    for element in array2:
        if element in hashTable:
            sharedElements.add(element)

    return sharedElements


def test_find_common():
    assert find_common([1, 2, 3, 8, 9, 10, 34, 6, 5, 3, 2], [3, 2, 5, 10, 22, 6, 43, 23, 8]) == set([2, 3, 5, 6, 8, 10])



