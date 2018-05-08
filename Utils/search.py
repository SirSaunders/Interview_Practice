def bSearch(sortedList, item):
    return binarySearch(sortedList, item, 0, len(sortedList))


def binarySearch(sortedlist, item, start, end):
    midPoint = ((end - start) / 2) + start
    midValue = sortedlist[midPoint]
    if item is midValue:
        return midPoint
    if end == midPoint or start == midPoint:
        return None  # item is not in list
    if midValue < item:
        return binarySearch(sortedlist, item, midPoint, end)
    else:
        return binarySearch(sortedlist, item, start, midPoint)


def test():
    aList = [123, 3, 2, 1, 8, 43543, 3, 23, 243,0, 4, 56, 57, 7, 6, 5, 4, 3, 2, 1, 3, 2, 33, 5, 67, 8, 4, 6, 5, 5, 4]
    aList.sort()
    print aList
    print('found at ' + str(bSearch(aList, 33)))  # should be 23
    print('found at ' + str(bSearch(aList, 43543)))  # should be 29

    print('found at' + str(bSearch(aList, 1)))  # should be 1 or 2 ( 2 items exist)
    print('found at ' + str(bSearch(aList, 0)))  # should be 0
    print('found at ' + str(bSearch(aList, 100)))  # should be None



