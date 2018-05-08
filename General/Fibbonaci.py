###Write fibbonaci iteratively and recursively (bonus: use dynamic programming)###

def fibbonaci_iteratively(index):
    a = 1
    b = 1 #starting numbers
    c = None
    if( index < 0 ):
        return None # must give a number greater than 0 as index
    # if less than index 2 then it must be 1
    if(index < 2):
        return a
    for i in range(1, index):
        c = a + b
        a = b
        b = c
    return c

print(fibbonaci_iteratively(0))
