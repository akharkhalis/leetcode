adress = '1.1.1.1'
counter = 0
ip = []
adress = adress + '.'
for i in adress:
    counter += 1
    print (counter, '-', i)
    if i == '.' or len(adress) < 1:
#        print (i)
        ipslot = adress[:counter-1]
#        print ('ipslot = ',ipslot)
        ip.append(ipslot)
        adress = adress[counter:]
        print('new adress =',  adress)
        counter = 0
        print('ip=' , ip)
print (ip[0] + '[.]' + ip[1] + '[.]' + ip[2] + '[.]'+ ip[3])