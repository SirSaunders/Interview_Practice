### big O(n)
def find_most_frequent(int_arr):
    hash_table = dict()

    for integer in int_arr:
        int_frequency = 0
        if integer in hash_table:
            int_frequency = hash_table[integer]
        hash_table[integer] = int_frequency + 1

    most_frequent_int = (None, 0)  # keep track of height frequency and the int that holds that frequency
    for integer in hash_table.keys():
        if hash_table[integer] > most_frequent_int[1]:
            most_frequent_int = (integer, hash_table[integer])
    return most_frequent_int  # return the int and its frequency


def test_finding():
    int_array = [2, 3, 4, 5, 6, 3, 1, 2, 3, 45, 6, 7, 8, 9, 77, 6, 5, 4, 32, 2, 4, 5, 6, 78, 7, 6, 54, 3, 2, 1, 34, 5,
                 7, 8]
    test = find_most_frequent(int_array)
    assert test == (6, 5)

    int_array = [1, 2, 3, 4, 2]
    test1 = find_most_frequent(int_array)
    assert test1 == (2, 2)

    # also is capable of working with strings, as python is dynamic typed
    int_array = [100, 2, 3, 4, 2, -2, -52, 'the', 56, 435, 23, 'the', 34243, 'the']
    test1 = find_most_frequent(int_array)
    assert test1 == ('the', 3)


test_finding()
