one = ['','one','two', 'three','four','five','six','seven','eight','nine']
ten = ['','twenty','thirty','forty','fifty','sixty', 'seventy','eighty','ninety']
hundred = 'hundred'
teen = ['ten', 'eleven', 'twelve', 'thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
hundreds = ["one",'two', 'three','four','five','six','seven','eight','nine']
one_sum = 0
teen_sum = 0
ten_sum = 0
hundred_sum = 0
total_sum = 0
#sum of teen's
for item in teen:
    teen_sum += len(item)
    print(item)
#sum of 2 digits and one's

for num in ten:
    for num_1 in one:
        ten_sum +=len(num)+len(num_1)
        print(num, num_1)
#sum of hundreds
for num in hundreds:
    for item in teen:
           hundred_sum += len(num) +len(hundred)+len("and")+len(item)
           print(num, "hundred and", item)
    for num_1 in ten:
        for num_2 in one:
            hundred_sum +=len(num)+ len(hundred)+len("and")+len(num_1)+len(num_2)
            print(num , "hundred and", num_1, num_2)
            if len(num_1)== 0 and len(num_2) ==0:
                hundred_sum -= 3

    
    """
    for num_1 in ten:
        for num_2 in one:
            hundred_sum += len(num_1)+len(num_2)
        if len(num)==0 and len(num_1) == 0:
            hundred_sum -= 3
            """
"""
for num in hundreds:
    for item in teen:
        hundred_sum += len(num) +len(hundred)+len("and")+len(item)
"""
total_sum = ten_sum+hundred_sum+teen_sum+one_sum+len("onethousand")
print(total_sum)