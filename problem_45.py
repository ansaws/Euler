n = 286
trinum = 0
c = 0
answer = 0
while True:
    trinum = n*(n+1)/2
    c = trinum*2
    if int((1+(1+12*c)**.5)/6) == (1+(1+12*c)**.5)/6 or int((1-(1+12*c)**.5)/6) == (1+(1+12*c)**.5)/6:
        c = trinum
        if int((1+(1+8*c)**.5)/4) == (1+(1+8*c)**.5)/4 or int((1-(1+8*c)**.5)/4) == (1+(1+8*c)**.5)/4:
          answer = trinum 
          break
    n +=1 
print(answer)