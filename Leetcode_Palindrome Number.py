def isPalindrome( x):
    if x < 0:
        print('isnot palindrome')
        return False

    revers = 0
    inp = x
    while revers <= x:
        last = x % 10
        x = int(x / 10)
        revers = revers * 10 + last
        print('x ', x)
        print('last ', int(last))
        print('revers ', revers)
        print('_______________next iteration')
        if revers == 0:
            if x == revers or x == int(revers / 10):
                print('is palindrome')
                return True
            else:
                print('isnot palindrome')
                return False

    if x == revers or x == int(revers / 10):
        print('is palindrome')
        return True
    else:
        print('isnot palindrome')
        return False

isPalindrome(10)