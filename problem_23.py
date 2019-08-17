abundant_num = []
abundant_num_sum = []
all_num = []
divisors = []
for num in range (1,round(28123)/2):
	ab_num = num
	for num_1 in range(1,ab_num):
		if num%num_1 == 0:
			divisors.append(num_1)
		if sum(divisors)> num:
			abundant_num.append(num)
	divisors = []
