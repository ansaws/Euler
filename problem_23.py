abundant_num = []
abundant_num_sum = 0
all_num = []
divisors = []
for num in range (28124):
	ab_num = num
	for num_1 in range(1,ab_num):
		if num%num_1 == 0:
			divisors.append(num_1)
		if sum(divisors)>num:
			abundant_num.append(num)
			break
	divisors = []

for num in abundant_num:
	for n in range(1, len(abundant_num)-1):
		for num_1 in range(n, len(abundant_num)):
			abundant_num_sum+=(num+ abundant_num[num_1])

for num in range(28124):
	all_num.append(num)


print(sum(abundant_num)-abundant_num_sum)