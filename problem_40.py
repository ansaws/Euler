"""
check = 1
prev_num = 1
num =1
count = 1
dig_min = [0,0]
dig_max = [0,0]
while check<1000001:
    while len(str(prev_num)) == len(str(num)):
        count+=1
        num+=1
    dig_min = dig_max
    dig_max = [len(str(num-1))*count, num]
    prev_num = num
    count = 0
    check*=10
"""
check =1
num = 1
leng =0
product = 1
prev_num = 1
temp= -1
while check<10000000:
    leng+=len(str(num))
    if leng ==1002:
        print("nothing")
    if leng>=check:
        print(num)
        print(int(str(num)[(leng-check)-1]))
        print(check)
        x = leng - len(str(num))
        while x!= check:
            x+=1
            temp+=1
        y = int(str(num)[temp])
        product*=y
        """int(str(num)[(leng-check)-1])"""
        check*=10
    elif leng == 3.1:
        print(num)
        print(int(str(prev_num)[-1]))
        print(check)
        product*=int(str(prev_num)[-1])
        check*=10
    num+=1
    prev_num = num-1
    temp = -1
print(product)