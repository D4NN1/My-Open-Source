def isPowerOfTwo(n):
    import math
    if math.log(n,2)%1 == 0:
        return 1
    else:
        return 0
isPowerOfTwo(536870912)