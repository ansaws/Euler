#success
'''
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
'''
Square_sum = 0
Sum_square= 0
num= 1
while num<101:
	Square_sum += num**2
	num+=1
num= 1
while num<101:
	Sum_square += num
	num+=1

x = Square_sum - Sum_square**2
print(x)
