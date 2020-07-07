#success
'''
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.


'''
final = 0
for num in range(100,1000):
	for num2 in range(100,1000):
		reverseNum = str(num*num2)
		reverseNum= reverseNum[::-1]
		if reverseNum == str(num*num2):
			if num*num2> final:
				final = num*num2
print(final)