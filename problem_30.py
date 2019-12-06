st = None
t1 = 0
total = 0
for num in range(4150,999999):
    st = str(num)
    for i in st:
        t1+=int(i)**5
    if t1== num:
        print(num)
        total+=num
    t1= 0
print(total)