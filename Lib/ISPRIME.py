def isPrime(num):
  prime = 0
  if num%2 != 0:
    for x in range(2,int(round(num**.5)+1)):
      if num%x ==0:
        prime+=1
        break
  if prime ==0:
    return True
  else:
    return False