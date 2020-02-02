"""
from decimal import Decimal
dec = None
f = 0
t = 0
count = {}
for num in range(11,1000,2):
    dec =  list(str(Decimal(1/num)))
    for de in range(2,len(dec)):
        if num<100:
            del dec[0:de]
        else:
            del dec[0:de]
        f = dec[0]
        for i in range(1,len(dec)):
            dig = dec[i]
            if dig==f:
                break
            else:
                t+=1
        count[t] = num
        t = 0
        dec =  list(str(Decimal(1/num)))
print(count[max(count.keys())])
"""
f_dig= 0
dig = 0
rem = 1
count = 0
max_count = 0
rem2= 1
max_num = 0 
for num in range(9,1000,2):
  while rem<num:
    rem =rem* 10
    count+=1
  f_dig = num//rem
  count +=1
  rem = num%rem
  rem2 = rem
  while f_dig != dig:
    while rem<num:
      rem = rem *10
      count +=1
    dig = num//rem
    count +=1
    rem = num%rem
    count+=1
  if count>=max_count:
    max_count = count
    max_num= num
  count = 0
  rem2 = rem
#switch the order of the floor division and also replace all tens and stuff its is 
print(max_count, max_num)