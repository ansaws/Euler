mult = 1
strNum = ""
lstNum= []
check = 0
panDig = 0
final = 0
for num in range(1,10000):
    while mult<10:
        strNum+=str(num*mult)
        panDig = int(strNum)
        if len(strNum)>9:
            break
        elif len(strNum) == 9:
            lstNum = sorted(strNum)
            for number in range(0,9):
                if lstNum[number] == str(number+1):
                    check+=1
            break
        mult+=1
    if check ==9 and final<panDig:
        print(num)
        final = panDig
    check = 0
    strNum = ""
    mult = 1
print(final)
