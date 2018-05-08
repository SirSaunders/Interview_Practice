###Write fibbonaci iteratively and recursively (bonus: use dynamic programming)###

def fibonaccii_iteratively(index):
    a = 1
    b = 1  # starting numbers
    c = None
    if (index < 0):
        return None  # must give a number greater than 0 as index
    # if less than index 2 then it must be 1
    if (index < 2):
        return a
    for i in range(1, index):
        c = a + b
        a = b
        b = c
    return c


def test_fibonacci_iteratively():
    assert fibonaccii_iteratively(0) == 1
    assert fibonaccii_iteratively(1) == 1
    assert fibonaccii_iteratively(2) == 2
    assert fibonaccii_iteratively(3) == 3
    assert fibonaccii_iteratively(4) == 5
    assert fibonaccii_iteratively(5) == 8
