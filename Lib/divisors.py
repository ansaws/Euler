def divisors(num):
	div = []
	for i in range(1,int(( num**1/2))+1):
		if num%i == 0:
			div.append(i)
	return div