#Check if String is a palindrome

def check_palindrome(string):
    string = string.replace(' ', '').lower() #removes whitespace and makes all chars lowercase
    for i in range(len(string)):
        if string[i] is not string[len(string)-i -1]:
            return False
    return True

def test_check_palindrome():
    assert (check_palindrome('race Car')==True)
    assert (check_palindrome('rbg')==False)

