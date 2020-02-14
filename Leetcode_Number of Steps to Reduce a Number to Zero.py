
def numberOfSteps(num):
    step = 0
    while num !=0:
        if (num % 2 ) == 0:
            num = num / 2
            step += 1
            print ( 'Even', num)
        if (num % 2) != 0:
            num = num - 1
            print ( 'odd', num)
            step += 1
    print (step)
numberOfSteps(123)