# Reverse a String iteratively and recursively

def reverse_iteratively(string):
    new_string = str()
    for char in reversed(string):
        new_string += char
    return new_string


def test_reverse_iteratively():
    assert reverse_iteratively('whats up') == 'pu stahw'

def reverse_recursively(string):
    print('')
    length = len(string)
    if length == 1:
        return string
    return string[length-1] + reverse_recursively(string[:-1])

def test_reverse_recursively():
    assert reverse_recursively('whats up') == 'pu stahw'


