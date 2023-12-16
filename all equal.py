def all_equal(a):
    a = list(a)
    a[0] = int(input('?'))
    a[1] = int(input('?'))
    a[2] = int(input('?'))
    if a[0] == a[1] == a[2]:
        print('true')
    else:
        print('false')




limp = [1,2,3]
all_equal(limp)
