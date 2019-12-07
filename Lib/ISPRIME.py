def isPrime(num):
	sum_prime=0
	isprime = None
	for x in range(2,num//2+1):
		if num%x ==0:
			break
		else:
			sum_prime+= 1
		if sum_prime == num//2-1:
			isprime = True
	if isprime == True:
		return True
	else:
		return False