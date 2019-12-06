import threading


def isPrime(num):
	sum_prime=0
	isprime = None
	for x in range(2,num//2+1):
		if num%x ==0:
			break
		else:
			sum_prime+= 1
		if sum_prime == num//2-1:
			isprime = True
	if isprime == True:
		return True
	else:
		return False


s_m_p = 29
def q1():
    t = 0
    c = 0
    c1 = 0
    for num in range(101,2500000000):
        sqrt = int(num**(1/2))
        for p in range(sqrt, num):
            c += 1
            if isPrime(p)==True and num%p ==0:
                break
            c1 += 1
        if c == c1:
            t +=1
        c =0
        c1=0
    print(t)
    return t
def q2():
    t2 = 0
    c1 = 0
    c2 = 0
    for num in range(2500000001,5000000000):
        sqrt = int(num**(1/2))
        for p in range(sqrt, num):
            c1 += 1
            if isPrime(p)==True and num%p ==0:
                break
            c2 += 1
        if c1 == c2:
            t2 +=1
        c1 =0
        c2=0
    print(t2)
    return t2
def q3():
    t2 = 0
    c1 = 0
    c2 = 0
    for num in range(5000000001,7500000000):
        sqrt = int(num**(1/2))
        for p in range(sqrt, num):
            c1 += 1
            if isPrime(p)==True and num%p ==0:
                break
            c2 += 1
        if c1 == c2:
            t2 +=1
        c1 =0
        c2=0
    print(t2)
    return t2
def q4():
    t2 = 0
    c1 = 0
    c2 = 0
    for num in range(7500000001,10000000000):
        sqrt = int(num**(1/2))
        for p in range(sqrt, num):
            c1 += 1
            if isPrime(p)==True and num%p ==0:
                break
            c2 += 1
        if c1 == c2:
            t2 +=1
        c1 =0
        c2=0
    print(t2)
    return t2
th1 = threading.Thread(target=q1)
th2 = threading.Thread(target=q2)
th3 = threading.Thread(target=q3)
th4 = threading.Thread(target=q4)


th1.start()
th2.start()
th3.start()
th4.start()

th1.join()
th2.join()
th3.join()
th4.join()
