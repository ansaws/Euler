#sucess
def d(num):
    sum = 0
    for num_1 in range(1, num):
        if num%num_1 == 0:
            sum += num_1
    return sum
sum = 0
for a in range(1,10001):
    b = d(a)
    if (a == d(b)) and (a != b):
        sum += a
print(sum)




