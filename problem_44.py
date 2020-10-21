pNums = [1]
possibleAns = []
count = 2
while len(possibleAns) == 0:
    pNums.append(count*(3*count -1)/2)
    for num in range(0, len(pNums)-2):
        checkSum = pNums[num] + pNums[len(pNums)-1]
        c = checkSum *2
        if int((1+(1+12*c)**.5)/6) == (1+(1+12*c)**.5)/6 or int((1-(1+12*c)**.5)/6) == (1+(1+12*c)**.5)/6:
            checkSum = pNums[len(pNums)-1] -pNums[num]
            c = checkSum *2
            if  int((1+(1+12*c)**.5)/6) == (1+(1+12*c)**.5)/6 or int((1-(1+12*c)**.5)/6) == (1+(1+12*c)**.5)/6:
                possibleAns.append(checkSum)
            else:
                continue
        else:   
            continue
    count+=1
print(possibleAns)