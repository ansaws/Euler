from Lib.ISPRIME import isPrime
from math import log10
primeSum = 0
numPrimes = 0
prime = 11
tempPrime = prime
check = False
while numPrimes<11:
    tempPrime =prime
    if isPrime(prime) == False:
        prime+=2
        continue
    while tempPrime>10:
        place = 10**(int(log10(tempPrime)))
        if isPrime(tempPrime - (tempPrime//place)*place) == False:
            check = True
            break
        tempPrime -= (tempPrime//place)*place
    if check ==True or isPrime(prime) == False:
        check = False
        prime+=2
        continue
    tempPrime= prime
    while(tempPrime>10):
        if isPrime(tempPrime //10) == False:
            check = True
            break  
        tempPrime = tempPrime //10
    if check == True or isPrime(prime) == False:
        check = False
        prime+=2
        continue
    primeSum+=prime
    numPrimes+=1
    print(prime)
    prime+=2
print("final: " + str(primeSum))
