numlist = []
binary = 0
total = 0
for num in range(1,1000000):
    numlist = list(str(num))
    if numlist != numlist[::-1]:
        continue
    binary = bin(num).replace("0b","")
    binary = list(binary)
    if binary != binary[::-1]:
        continue
    total += num
print(total)
    





