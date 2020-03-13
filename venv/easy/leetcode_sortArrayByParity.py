data = [1,2,3,4,5,6]

b = []
for i in data:
    if i % 2 == 0:
        print (i)
        b.insert(0,i)
    else:
        b.insert((len(b) - 1),i)
    print(b)


