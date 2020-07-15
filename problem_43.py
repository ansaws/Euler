primes = [2,3,5,7,11,13,17]
ans = 0
for num in range(1000000000,10000000000):
    check = 0
    count = 0
    if sorted(str(num)) != sorted("0123456789"):
        continue
    while count<len(primes):
        strNum = str(num)
        strNum = strNum[count+1:count+4]
        intNum = int(strNum)
        if intNum%primes[count] != 0:
            check = 1
            break
        count+=1
    if check ==0:
        print(num)
        ans+=num

