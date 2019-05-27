""""
d = {}
sum = 0
for num in range(2,10000):

    d[num] = sum
    sum = 0
sum = 0
d[1] = 1

for num in d:
    x = d[num]
    if d[x]==num:
        sum+=num
print(sum-1)
"""

def d(num):
    sum = 0
    for num_1 in range(1, num):
        if num%num_1 == 0:
            sum += num_1
    return sum

sum = 0
for a in range(1,10001):
    b = d(a)
    if a == d(b):
        sum += a





