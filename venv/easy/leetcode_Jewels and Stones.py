def numJewelsInStones(J, S):
    jewels_counter = 0
    for jewels in J:
        #        print (jewels)
        for stones in S:
            if stones == jewels:
                jewels_counter += 1
    print (jewels_counter)
    return jewels_counter


#numJewelsInStones ("aA", "aAAbbbb")
numJewelsInStones ("zZa", "ZZZAAAAAAAAaz")
