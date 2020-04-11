def isPrime(num):
  """
  sum_prime=0
  isprime = None
  for x in range(2,num//2+1):
    if num%x ==0:
      break
    else:
      sum_prime+= 1
    if sum_prime == num//2-1:
      isprime = True
  if num == 2 or num ==3:
    return True
  elif isprime == True:
    return True
  else:
    return False
  """
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
print(isPrime(73))