# Find the first non-repeated character in a String

#this is case sensitive if you need a non-casesensitive version just make all of the chars upper or lower case
def find_first_non_repeat(string):
    hashTable = dict()
    # add all chars into hashtable with their frequencies
    for char in string:
        if char not in hashTable:
            hashTable[char] = 1
        else:
            hashTable[char] += 1

    for char in string:
        if hashTable[char] is 1:
            return char

    return None

def test_find_first_non_repeat():
    assert (find_first_non_repeat('hi my name is john')=='y')
    assert (find_first_non_repeat('this is Big O(n)')=='t')
    assert (find_first_non_repeat('bear Bee') == 'b') #shows case sensitivity


