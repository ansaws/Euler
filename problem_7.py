#sucess
'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
'''
num = 3
prime_numbers = [2]
prime = 0
prime_1 = 0
while len(prime_numbers)< 10001:
    if num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                prime_1 = i-1
                break
            else:
                prime_1 = i-1
                prime = prime+1
        if prime == prime_1:
            prime_numbers.append(num)
            print(num)
    num+=1
    prime = 0
    prime_1 = 0

