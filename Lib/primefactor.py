from lib.ISPRIME import isPrime
def pFactor(num):
    final = {}
    nonPrime = num
    div = 2
    if isPrime(num) == True:
        isPrime.append(num)
        return final
    while isPrime(nonPrime) == False:
        while nonPrime%div !=0 and isPrime(div) == False:
            div+=1
        if(final.has_key(div)):
            final[div] +=1
        else:
            final[div] = 1
        nonPrime /=div
        div = 2 
     if(final.has_key(nonPrime)):
            final[nonPrime] +=1
    else:
        final[nonPrime] = 1
    return final
