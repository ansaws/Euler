def isprime(num):
	sum_prime=0

	for x in range(2,int(round(num**(1/2)))+1):
		if num%x ==0:
			break
		else:
			sum_prime+= 1
		if sum_prime == int(round(num**(1/2))-1):
			return True

len_1 = 0
max_num = 0
for num in range(2,1000):
	if isprime(num)==True:
		dig = 10//num
		c_dig = dig+1
		len = 0
		rem = 10%num
		while c_dig != dig:
			c_dig-=1
			len += 1
			c_dig = (rem*10)//num
			if rem == 0:
				break
			rem = (rem*10)%num
		if len> len_1:
			len_1 = len
			max_num= num
		
print(max_num)



