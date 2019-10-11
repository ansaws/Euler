start = 25
sum = 101
dim = 6
while dim<1002:
    for x in range(1,5):
        start+=dim
        sum+=start
    dim +=1
print(sum)