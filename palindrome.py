while True:
    ppalind = str(input('?'))
    ppalind = list(ppalind)
    if (ppalind == ppalind[::-1]):
        print('string is a palindrome')
    else:
        print('string is nota palindrome')
    check = str(input('do you wnat to check again -- Y or N'))
    if check == 'Y':
        continue
    print('bye')
    break
