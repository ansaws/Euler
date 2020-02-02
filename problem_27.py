from Lib.EulerFormula import ef
from Lib.ISPRIME import isPrime
primes = 0
max_prime = [0, 0]
for a in range(-999,1000):
  for b in range(-1000, 1001):
    for n in range(10000000):
      if isPrime(ef(a,b,n)) == False:
        break
      else:
        primes +=1
    if primes> max_prime[0]:
      max_prime[0]=primes
      max_prime[1] = a*b
    primes = 0
print(max_prime)
