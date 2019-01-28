import time

start_time = time.time()
num = 4
sum_prime = 5
while num<2000000:
    for div in range (2, round(num**.5)+1):
        if num%div == 0:
            break
        if div == round(num**.5):
            sum_prime += num
    num+=1
    #print(num)

print(sum_prime)

print("Time took to run the program: " + str(time.time()-start_time))