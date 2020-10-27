from Lib.ISPRIME import isPrime
count = 25
cCheck = 0
check = 1
diff = 0
while True:
    cCheck = 0
    if isPrime(count) == True:
        count +=2
        check = 1
        continue
    diff = count-(2*(check**2))
    if(diff<0):
        break
    if isPrime(diff) == True:
        count +=2
        check = 1
        continue
    check +=1
    while True:
        diff = count-(2*(check**2))
        if(diff<0):
            break
        if isPrime(diff) == True:
            count +=2
            check = 1
            break
        check +=1
    if cCheck>check:
        break
print(count)



        
        