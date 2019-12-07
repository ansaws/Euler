num = 0
nums= []
t1= 0
for a in range(1, 100):
    for b in range(1, 100):
        num = a**b
        for i in str(num):
            t1 += int(i)
            nums.append(t1)
        t1=0
print(max(nums))