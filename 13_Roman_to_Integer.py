s = "LVIII"
def romanToInt(s):
    arabic = 0
    roman_dict={
        'I':'1',
        'V':'5',
        'X':'10',
        'L':'50',
        'C':'100',
        'D':'500',
        'M':'1000'
    }
    print (type(roman_dict))
    roman = s.split()
    for i in range(s):
        print (i)
        if s[i] in ('V','X'):
            if s[i-1] == 'I':
                arabic -= 1
        elif s[i] in ('L','C'):
            if s[i - 1] == 'X':
                arabic -= 10
        elif s[i] in ('D','M'):
            if s[i - 1] == 'C':
                arabic -= 100
        for key in roman_dict:
            if s[i] == key:
                print (roman_dict[key])
                arabic += int(roman_dict[key])
                print (arabic)


romanToInt(s)


# def romanToInt(self, s: str) -> int:
#     roman = {
#         "I": 1,
#         "V": 5,
#         "X": 10,
#         "L": 50,
#         "C": 100,
#         "D": 500,
#         "M": 1000,
#     }
#     number = roman[s[0]]
#     for i in range(1, len(s)):
#         if ((s[i] == "V" or s[i] == "X") and s[i - 1] == "I") or ((s[i] == "L" or s[i] == "C") and s[i - 1] == "X") or (
#                 (s[i] == "D" or s[i] == "M") and s[i - 1] == "C"):
#             number = number - 2 * roman[s[i - 1]]
#         number += roman[s[i]]
#     return number
