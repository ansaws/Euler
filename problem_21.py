d = {}
sum = 0
for num in range(1,6):
    for num_1 in range(1, num):
        if num%num_1 == 0:
            sum += num_1
    d[num] = sum
    sum = 0
for num in 

