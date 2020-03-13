
def romanToInt(s):
    roman_dict = {'I':1,'V':5, 'X':10,'L':50,'C':100,'D':500,'M':1000}
    numbers = 0
    for i in s:
        numbers += roman_dict[i]
#    for i in numbers:
#        sum += numbers[i]
    print (numbers)
    print (sum)
    if

romanToInt('XXI')
# I can be placed before V (5) and X (10) to make 4 and 9.
# X can be placed before L (50) and C (100) to make 40 and 90.
# C can be placed before D (500) and M (1000) to make 400 and 900.