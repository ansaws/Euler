one = ['one','two', 'three','four','five','six','seven','eight','nine','']
ten = ['twenty','thirty','fourty','fifty','sixty', 'seventy','eighty','ninety','']
hundred = 'hundred'
teen = ['ten', 'eleven', 'twelve', 'thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
one_sum = 0
teen_sum = 0
ten_sum = 0
hundred_sum = 0
total_sum = 0
#sum of teen's
for item in teen:
    teen_sum += len(item)
    hundred_sum += len(item) +len(hundred) +3
#sum of 2 digits and one's
"""
for num in ten:
    for num_1 in one_1:
        ten_sum +=len(num)+len(num_1)
"""
#sum of all but one's and teen's
for num in one:
    for num_1 in ten:
        for num_2 in one:   
            if len(num) == 0:
                hundred_sum += -(len(hundred)+3) 
            if len(num_1)==0 or len(num_2) == 0:
                hundred_sum += -3
            hundred_sum += len(num) + len(hundred) + 3 + len(num_1) + len(num_2) 

total_sum = ten_sum+hundred_sum+teen_sum-6
print(total_sum)