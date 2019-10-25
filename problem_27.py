def isprime(num):
	sum_prime=0

	for x in range(2,num//2+1):
		if num%x ==0:
			break
		else:
			sum_prime+= 1
		if sum_prime == num//2-1:
			return True
primes = 0
a_current = 0
b_current = 0
primes_current = 0
n =0 
for a in range(-999,1000):
	if isprime(a) == True:
		for b in range(-1000,1001):
			if isprime(b) == True:
				while True:
					t= isprime(n**2 + a*n + b)
					if t == True:
						#print(n**2+a*(n)+b)
						primes_current+=1
						n+=2
					else:
						n=0
						break
				if primes_current>primes:
					primes = primes_current
					a_current = a
					b_current = b
				primes_current = 0

print(a_current*b_current)
