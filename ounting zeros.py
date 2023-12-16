b = 1000000001001
def trailing_zeros(longint):
    manipulandum = str(longint)
    x = 0
    i = 1
    for ch in manipulandum:
        if manipulandum[-i] == '0':
            x += x
            i += 1
        else:
            print (x)
trailing_zeros(b)
