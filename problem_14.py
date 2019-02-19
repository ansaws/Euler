#sucess
coll = 0
len_coll = 0
lengths = {}
for num in range(1, 1000000):
    coll = num
    while True:
        if num%2 == 0:
            num = num/2
            len_coll +=1
        if num ==1:
            lengths[len_coll]=coll
            break
        if num%2 == 1:
            num = (3*num)+1
            len_coll += 1
    len_coll = 0

sor_lengths = sorted(lengths.keys())

max_length = sor_lengths[len(sor_lengths)-1]

print(lengths[max_length])