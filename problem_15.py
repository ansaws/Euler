import math
def double_factorial(x):
	total = 1
	factors = []
	for num in range(x, 0, -2):
		factors.append(num)
	for factor in factors:
		total *= factor
	return total
z = double_factorial(39)
y = (2**20)*z
final = y/(math.factorial(20))
print(final)

		