#success
'''
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

'''

products = []
for num in range(100,1000):
	for number in range(100,1000):
		products.append(num*number)



palindrome = []
palindromes = []
for num_1 in products:
	numbers = list(map(int,str(num_1)))
	num_2 = list(reversed(numbers))
	if numbers == num_2:
		palindromes.append(num_1)

palindrome = sorted(palindromes)
print(palindrome[len(palindrome)-1])

