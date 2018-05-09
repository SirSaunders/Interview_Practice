# Check if a String is composed of all unique characters
def check_all_unique(string):
    hashtable = dict()
    # add all chars to hashtable for their frequency
    for char in string:
        if (char not in hashtable):
            hashtable[char] = 1
        else:
            hashtable[char] += 1
            # check if all chars only occured once
    for char in hashtable.keys():
        if hashtable[char] is not 1:
            return False

    return True

def test_check_all_unique():
    assert (check_all_unique('qwertyuio')==True)
    assert(check_all_unique('qwertdqyuio')==False)
