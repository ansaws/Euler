#sucess
import math
st = None
t1 = 0
total = 0
for num in range(10,999999):
    st = str(num)
    for i in st:
        t1+= math.factorial(int(i))
    if t1 == num:
        print(num)
        total += num
    t1=0
print(total)
