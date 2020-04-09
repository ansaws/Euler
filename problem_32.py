splitlist = []
products = []
check = ["1", "2", "3", "4", "5","6", "7", "8", "9"]
sum = 0
for num in range(1, 10000):
    for num2 in range(1,1000):
        splitlist = list(str(num))+list(str(num2))+ list(str(num*num2))
        if len(splitlist) <9:
            continue
        if len(splitlist) >9:
            break
        if sorted(splitlist) == check:
            if num*num2 in products:
                continue
            else:
                sum+=num*num2
            products.append(num*num2)
print(sum)