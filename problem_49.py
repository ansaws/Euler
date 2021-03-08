
from Lib.ISPRIME import isPrime
from itertools import permutations
from Lib.listtostr import strl
num = 1487
found = False
answer = 0
perms = []
numbers =[]

try:
    while found == False and num<10000:
        num+=1
        if(isPrime(num) == False):
            continue
        perms =  list(permutations(list(str(num))))
        numbers = []
        for x in perms:
            if(isPrime(int(strl(x)))) and int(strl(x))>1000:
                numbers.append(x)
        perms = list(set(numbers))
        for item in range(0,len(perms)):
            perms[item] = int(strl(perms[item]))
        perms = sorted(perms)
        for j in range(1, len(perms)):
            for k in range(j+1, len(perms)):
                inum = num
                jnum = perms[j]
                knum = perms[k]
                if (jnum-inum) == (knum-jnum):
                    answer  = str(num)+str(jnum)+str(knum)
                    print(numbers)
                    print(inum)
                    print(jnum)
                    print(knum)
                    found = True
                    break
            if found:
                break
        if found:
            break
    print(answer)
except:
    print("error")
