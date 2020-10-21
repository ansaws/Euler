from Lib.listtostr import strl

primes = [2,3,5,7,11,13,17]
ans = 0

def permutation(lst): 
    if len(lst) == 0: 
        return [] 
    if len(lst) == 1: 
        return [lst] 
    l = [] 
    for i in range(len(lst)): 
       m = lst[i]  
       remLst = lst[:i] + lst[i+1:] 
       for p in permutation(remLst): 
           l.append([m] + p) 
    return l 
panDig = permutation(['0','1','2','3','4','5','6','7','8','9'])
for i in range(0, len(panDig)):
    panDig[i] = strl(panDig[i])

for num in panDig:
    check = 0
    count = 0
    while count<len(primes):
        strNum = num
        strNum = strNum[count+1:count+4]
        intNum = int(strNum)
        print(num)
        if intNum%primes[count] != 0:
            check = 1
            break
        count+=1
    if check ==0:
       print(num)
       ans+=int(num)

print(ans)