s = "1326#"
output = []
inp_len = len(s) - 1
while inp_len >= 0:
   if s[inp_len] == '#':
       output.append(chr(96+int(s[inp_len-2:inp_len])))
       inp_len -= 3
       print (output)
   else:
       output.append(chr(96+int(s[inp_len])))
       inp_len -= 1
       print(output)
print ("".join(output[::-1]))

