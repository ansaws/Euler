from Lib.ISPRIME import isPrime
splitlist = []
rotate = 0
rotated = 0
prime = 0
total = 0
for num in range(3,1000000,2):
    if isPrime(num) == False:
        continue
    prime+=1
    splitlist = list(str(num))
    for i in range(len(splitlist)-1):
        rotate = splitlist[0]
        splitlist.remove(rotate)
        splitlist.append(rotate)
        thingy = ""
        rotated = int(thingy.join(splitlist))
        if rotated %2 == 0:
            break
        if isPrime(rotated) == False:
            break
        prime +=1
    if prime == len(splitlist):
        total+=1
    prime = 0
print(total+1)


