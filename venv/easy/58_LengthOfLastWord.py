def lengthOfLastWord(s):
    txt = s.split()
    if len(txt) > 0:
        ol = len(txt[-1])
        return ol
    else:
        return (0)

print (lengthOfLastWord("welcome to the jungle"))