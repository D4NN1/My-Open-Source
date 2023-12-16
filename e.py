n = int(input())
def factorial(n):
    if n == 1 or n == 0:
        return 1
    else: 
        return n * factorial(n-1)
total = 0
total = float(total)
for i in range(n):
    total = total + ((1/(factorial(i))))
    print(total)
    