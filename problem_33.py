from fractions import Fraction
numbers45 = []
combined = []
div = []
for num in range(10,100):
    for num5 in range(10,100):
        if num == num5:
            continue
        if num%10 ==0 and num5%10==0:
            continue    
        combined = list(str(num))+ list(str(num5))
        for element in combined:
            if combined.count(element) >1:
                combined.remove(element)
                combined.remove(element)
        if len(combined) == 2 and combined[1] != "0":
            if int(combined[0])/int(combined[1]) == num/num5:
                numbers45.extend([num , num5])
                if num/num5>1:
                    div.append(num/num5)
product = 1
for num in div:
    product*=num
print(product)