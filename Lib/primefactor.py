def isPrime(num):
  prime = True
  if num%2 != 0:
    for x in range(2,int(round(num**.5)+1)):
      if num%x ==0:
        prime = False
        break
  else:
    prime = False
  if num ==1:
    prime = False
  if num ==2:
    prime = True
  return prime

def pFactor(num):
    final = {}
    nonPrime = num
    div = 2
    if isPrime(num) == True:
        final[num] = 1
        return final
    while isPrime(nonPrime) == False:
        while nonPrime%div !=0:
            div+=1
        if div in final.keys():
            final[div] +=1
        else:
            final[div] = 1
        nonPrime /=div
        div = 2 
    nonPrime = int(nonPrime)
    if nonPrime in final.keys():
        final[nonPrime] +=1
    else:
        final[nonPrime] = 1
    return final
