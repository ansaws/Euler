from decimal import Decimal
dec = None
f = 0
t = 0
count = {}
for num in range(11,1000,2):
    dec =  list(str(Decimal(1/num)))
    if num<100:
        del dec[0:4]
    else:
        del dec[0:3]
    f = dec[0]
    for i in range(1,len(dec)):
        dig = dec[i]
        if dig==f:
            break
        else:
            t+=1
    count[t] = num
    t = 0
print(Decimal(1/321))
print(count[max(count.keys())])
