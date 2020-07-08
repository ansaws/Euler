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