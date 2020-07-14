from Lib.ISPRIME import isPrime
ans = 0
for num in range(2143,1000000000,2):
    if num%2==0 or str(num)[-1] ==5 or str(num)[-1] ==9:
        continue
    strNum = str(num)
    strNum = sorted(strNum)
    checkStr = []
    for string in range(1,len(strNum)+1):
        checkStr.append(str(string))
    if strNum !=checkStr:
        continue
    if isPrime(num) == False:
        continue
    ans = num
    print(ans)
print(ans)