###Write fibbonaci iteratively and recursively (bonus: use dynamic programming)###
import datetime


def fibonaccii_iteratively(index):
    a = 0
    b = 1  # starting numbers
    c = None
    if (index <= 0):
        return a  # must give a number greater than 0 as index
    # if less than index 2 then it must be 1
    if (index < 2):
        return b
    for i in range(1, index):
        c = a + b
        a = b
        b = c
    return c


def test_fibonacci_iteratively():
    assert fibonaccii_iteratively(0) == 0
    assert fibonaccii_iteratively(1) == 1
    assert fibonaccii_iteratively(2) == 1
    assert fibonaccii_iteratively(3) == 2
    assert fibonaccii_iteratively(4) == 3
    assert fibonaccii_iteratively(5) == 5


def fibonacci_recursively(index):
    if index <= 0:
        return 0
    if index < 2:
        return 1
    return fibonacci_recursively(index - 2) + fibonacci_recursively(index - 1)


def test_fibonacci_recursively():
    assert fibonacci_recursively(0) == 0
    assert fibonacci_recursively(1) == 1
    assert fibonacci_recursively(2) == 1
    assert fibonacci_recursively(3) == 2
    assert fibonacci_recursively(4) == 3
    assert fibonacci_recursively(5) == 5


hashTable = dict()


def fibonacci_recursively_dynamic(index):
    if index <= 0:
        return 0
    if index < 2:
        return 1
    if index not in hashTable:
        hashTable[index] = fibonacci_recursively_dynamic(index - 2) + fibonacci_recursively_dynamic(index - 1)
    return hashTable[index]


def test_fibonacci_recursively_dynamic():
    assert fibonacci_recursively_dynamic(0) == 0
    assert fibonacci_recursively_dynamic(1) == 1
    assert fibonacci_recursively_dynamic(2) == 1
    assert fibonacci_recursively_dynamic(3) == 2
    assert fibonacci_recursively_dynamic(4) == 3
    assert fibonacci_recursively_dynamic(5) == 5

#showing the time comparision of each solution
def show_time_comparison():
    start = datetime.datetime.now()
    print(fibonaccii_iteratively(35))
    print('fibonaccii_iteratively finished in: ' + str(datetime.datetime.now() - start))
    start = datetime.datetime.now()
    print(fibonacci_recursively(35))
    print('fibonacci_recursively finished in: ' + str(datetime.datetime.now() - start))
    start = datetime.datetime.now()
    print(fibonacci_recursively_dynamic(35))
    print('fibonacci_recursively_dynamic finished in: ' + str(datetime.datetime.now() - start))

show_time_comparison()