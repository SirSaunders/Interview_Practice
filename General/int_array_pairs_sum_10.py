###################### worst way: Big O(n^2) #############################
def worst_find_pair_sum(int_arry, target):
    pairs = []
    for i in range(len(int_arry)):  # move up array
        x = int_arry[i]
        for j in reversed(range(len(int_arry))):  # move down array
            y = int_arry[j]
            if i is j:  # if i is j then all possible pairs for i have be checked move to next, no need to check
                # previous indexes below i
                break
            if x + y == target:
                pairs.append((i, j, x, y))  # append the position indexes and their numbers
    return pairs


def test_worst():
    assert worst_find_pair_sum([1, 2, 3, 4, 5, 6, 7, 8, 9], 10) == [(0, 8, 1, 9), (1, 7, 2, 8), (2, 6, 3, 7),
                                                                    (3, 5, 4, 6)]
    assert worst_find_pair_sum([1, 2, 5, 3, 4, 5, 6, 7, 8, 9], 10) == [(0, 9, 1, 9), (1, 8, 2, 8), (2, 5, 5, 5),
                                                                       (3, 7, 3, 7), (4, 6, 4, 6)]


############# Better Method: Big O(n log n) ###############################
# # suggested giving a presorted list, else the first 2 returned values wont match what was sent. But the pairs will
# be correct this has a Big O(n Log n) because sorting (tim sort) is Big o(n Log n) and binary search is big O(log n),
# only keep the dominant so just keep the search of ""Big O( n Log n)""
def mid_find_pair_sum(int_arry, target):
    pairs = []
    int_arry.sort()
    for i in range(len(int_arry)):  # move up array
        x = int_arry[i]
        compliment = target - x
        # find compliment with  binary search
        found_compliment = Interview_Practive.Utils.search.bSearch(int_arry, compliment)
        if found_compliment:
            y = int_arry[found_compliment]
            pairs.append((i, found_compliment, x, y))
    return pairs


def test_mid():
    assert mid_find_pair_sum([1, 2, 3, 4, 5, 6, 7, 8, 9], 10) == [(0, 8, 1, 9), (1, 7, 2, 8), (2, 6, 3, 7),
                                                                  (3, 5, 4, 6)]
    assert mid_find_pair_sum([1, 2, 5, 3, 4, 5, 6, 7, 8, 9], 10) == [(0, 9, 1, 9), (1, 8, 2, 8), (2, 7, 3, 7),
                                                                     (3, 6, 4, 6), (4, 5, 5, 5)]


############# Best Method: Big O(n) ###############################
def best_find_pair_sum(int_arry, target):
    pairs = []
    hashTable = dict()
    # add all of items into a hashTable
    for item in int_arry:
        hashTable[item] = True
    print hashTable
    for i in range(len(int_arry)):  # move up array
        x = int_arry[i]
        compliment = target - x
        # look up compliment in hash table if it exists
        found_compliment = None
        if compliment in hashTable:
            found_compliment = compliment
        if found_compliment and x is not found_compliment:
            pairs.append((x, found_compliment))
    return pairs


def test_best():
    assert best_find_pair_sum([1, 2, 3, 4, 5, 6, 7, 8, 9], 10) == [(1, 9), (2, 8), (3, 7), (4, 6), (6, 4), (7, 3),
                                                                   (8, 2), (9, 1)]
