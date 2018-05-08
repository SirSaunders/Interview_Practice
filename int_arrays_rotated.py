def check_rotation(array1, array2):
    if len(array1) is not len(array2):
        return False
    array1.extend(array1)  # concat an array to itself
    if isSubList(array1, array2):
        return True
    else:
        return False


def isSubList(array1, array2):
    i = 0
    for e in array1:
        if (e is not array2[i]):
            i = 0
        if (i is len(array2) - 1):
            return True
        i += 1
    return False


def test_rotation():
    a = [1, 2, 3, 1, 5]
    b = [3, 1, 5, 1, 2]
    c = [4, 5, 3, 2, 1]
    d = [4, 5, 3, 2, 1, 5]

    assert (check_rotation(b, a) == True)
    assert (check_rotation(b, c) == False)
    assert (check_rotation(b, d) == False)
