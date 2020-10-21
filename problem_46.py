from Lib.ISPRIME import isPrime
num = 27
chnum = 0
found = False
checkSq = 1
check = 1
while found == False:
    checkSq =1
    check = 1
    chnum = num
    if(isPrime(num) == True):
        num+=2
        continue
    else:
        while num>(checkSq**2)*2:
            if isPrime(num-(checkSq**2)*2) == True:
                num+=2
                break
            else:
                check+=1
            checkSq+=1
        if(check == (checkSq**2)*2):
            found = True
            print(checkSq)
            print(num)