# Determine if 2 Strings are anagrams

def check_anagrams(str1, str2):
    if (len(str1) is not len(str2)):
        return False
    hashTable1 = dict()
    hashTable2 = dict()

    # add all of string 1 and string 2 char frequencies to hash table
    for i in range(len(str1)):
        char1 = str1[i]
        char2 = str2[i]
        # add char1 to hashtable1
        if char1 not in hashTable1:
            hashTable1[char1] = 1
        else:
            hashTable1[char1] += 1
        # add char2 to hashtable2
        if char2 not in hashTable2:
            hashTable2[char2] = 1
        else:
            hashTable2[char2] += 1
    ### may be better to make a separate method to make hashtable 1 and 2 from the strings. would reduce duplicaiton
    return hashTable1 == hashTable2

def test_check_anagrams():
    assert (check_anagrams('hi you', 'you hi') == True)
    assert (check_anagrams('hi you', 'you to') == False)




