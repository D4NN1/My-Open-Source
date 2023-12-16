import math
def isPowerOfTwo(n):
    a = math.log(n,2)
    b = int(math.log(n,2))
    return a==b
print(isPowerOfTwo(16))
