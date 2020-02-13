num = -124
revers = 0
absnum = abs(num)
while absnum != 0:
    last = absnum % 10
    absnum = int(absnum / 10)
    if absnum < 0:
        revers = (revers * 10 + last)
    else:
        revers = revers * 10 + last
    print (last)
    print (revers)