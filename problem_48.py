total  = 0
for num in range(1, 1001):
    total += num**num
strtotal= str(total)
print(strtotal[len(strtotal)-10:])