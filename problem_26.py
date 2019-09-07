def isprime(num):
	sum_prime=0
	for x in range(2,int(round(num**(1/2)))+1):
		if num%x ==0:
			break
		else:
			sum_prime+= 1
		if sum_prime == int(round(num**(1/2))):
			return True
for num in range(2,1000):
	if isprime(num)==True:
		print("")