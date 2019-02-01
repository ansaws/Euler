len_coll = 0
lenghths = []
numbers = []
for num in range(1, 100000):
    while True:
        if num%2 == 0:
            num = num/2
            len_coll +=1
        if num ==1:
            lenghths.append(len_coll)
            break
        if num%2 == 1:
            num = (3*num)+1
            len_coll += 1
    print(len(lenghths))
lenghths = sorted(lenghths)

print(len(lenghths))