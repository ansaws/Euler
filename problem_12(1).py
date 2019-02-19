import time

start_time = time.time()
num = 1
tri_num = 0
divisors = 1
while True:
    for number in range(1,num+1):
        tri_num += number
    if num%2 == 0:
        for div in range(1,round(tri_num/2)):
            if tri_num % div == 0:
                divisors +=1
    if num%2 == 1:
        for div in range(1,round(tri_num/2),2):
            if tri_num % div == 0:
                divisors +=1
    if divisors > 500:
        break
    tri_num = 0
    divisors = 1
    num+=1

print(tri_num)
print(' ')
print(time.time()-start_time)

