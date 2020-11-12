from Lib.primefactor import pFactor
num = 10
found = 0
num_pFactor = {}
check_pFactor = {}
num_pair= []
check_pair = []
addFound = True
while found<3:
    found = 0
    num +=1
    num_pFactor = pFactor(num)
    if(len(num_pFactor.keys()) ==4):
        for check in range(num+1, num +4):
            check_pFactor = pFactor(check)
            if(len(check_pFactor.keys()) ==4):
                for num_key in num_pFactor.keys():
                    num_pair = [num_key, num_pFactor[num_key]]
                    for check_key in check_pFactor.keys():
                        check_pair = [check_key, check_pFactor[check_key]]
                        if(check_pair == num_pair):
                            addFound = False
                if(addFound == False):
                    break
                else:
                    found +=1
            else:
                break

print(num)


            
        
        


