#success
'''
Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
'''



num = 1
sum = 0
prev_1 = 1
prev_2 = 1

while num<4000000:
    if num%2 == 0:
        sum += num
    prev_2 = num
    num += prev_1
    prev_1 = prev_2

print(sum)






















