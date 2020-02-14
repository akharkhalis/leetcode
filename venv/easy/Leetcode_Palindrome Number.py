def isPalindrome(x):
    if x < 0:
        return False

    revers = 0
    inp = x
    while revers <= x:
        last = x % 10
        x = int(x / 10)
        revers = revers * 10 + last
        if revers == 0:
            if x == revers or x == int(revers / 10):
                return True
            else:
                return False

    if x == revers or x == int(revers / 10):
        return True
    else:
        return False

isPalindrome(10)