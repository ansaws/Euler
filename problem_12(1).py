import time

start_time = time.time()
num = 8
tri_num = 0
divisors = 0
while True:
    for number in range(1,num+1):
        tri_num += number
    for div in range(1,tri_num+1):
        if tri_num % div == 0:
            divisors +=1
    if divisors == 500:
        break
    tri_num = 0
    divisors = 0
    num+=1

print(tri_num)
print(' ')
print(time.time()-start_time)



    