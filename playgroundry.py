import tkinter
a,b,*c,d = ('ni','ch','pa','bys','ki','no')
print(c)

first = {1, 2, 3, 4, 5, 6}
second = {4, 5, 6, 7, 8, 9}

print(first | second)
print(first & second)
print(first - second)
print(second - first)
print(first ^ second)
def my_func(f, arg):
  return f(arg)
def factorial(x):
    if x == 1:
        return 1
    else: 
        return x * factorial(x-1)
for x in range(3,6):
    print(factorial(x))

for i in range(5):
   print(my_func(lambda x : x**2, i))


def isprime(x):
    i = 3
    if x == 1:
        return False
    if x == 2:
        return True
    if x%2  == 0 and x!=2:
        return False
    if x%3 == 0:
        return False
    else:
        while i < x:
            if x%i == 0:
                return False
            else:
                return True
        i = i + 1
while True:
    a = int(input('your number'))
    print(isprime(a))
   
