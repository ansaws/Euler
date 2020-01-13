from Lib.ISPRIME import isPrime as isprime

"""
def isprime(num):
	sum_prime=0

	for x in range(2,int(round(num**(1/2)))+1):
		if num%x ==0:
			break
		else:
			sum_prime+= 1
		if sum_prime == int(round(num**(1/2))-1):
			return True
#################################################
len_1 = 0
max_num = 0
for num in range(2,1000):
	if isprime(num)==True:
		dig = 10//num
		c_dig = dig
		len = 0
		rem = 10%num
		while c_dig != dig:
			c_dig-=1
			len += 1
			c_dig = (rem*10)//num
			if rem == 0:
				break
			rem = (rem*10)%num
		if len> len_1:
			len_1 = len
			max_num= num

print(max_num)


f_dig= 0
dig = 0
rem = 0
count = 0
max_count = 0

for num in range(9,1000,2):
  print(num)
  f_dig = 10//num
  count +=1
  rem = num%1
  if num<10:
    while f_dig != dig:
      print(1)
      dig = 10//rem
      count +=1
      rem = 10%dig
      count+=1
    if count>=max_count:
      max_count = count
    count = 0
  if num>9 and num<100:
    while f_dig != dig:
      print(1)
      dig = 100//rem
      count +=1
      rem = 10%dig
      count+=1
    if count>=max_count:
      max_count = count
    count = 0

    
print(max_count)
#Code in stuff for zero next time(when the first thing is zero and needs to be exteneded)
"""
dec = None
for num in range(11,1000,2):
    dec =  list(str(1/num))
    if num<100:
        del dec[0-3]
    else:
        del dec[0-4]


