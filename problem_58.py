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


prime = [3,5,7]
diag = [1,3,5,7]
inc = 4
num = 9
while len(prime)/len(diag) >= .1:
    for i in range(4):
        if isPrime(num) == True:
            prime.append(num)
        diag.append(num)
        num+= inc
    inc+=2
print(diag[-1]-diag[-2]-1    )  
