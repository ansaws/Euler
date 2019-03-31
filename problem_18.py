all =   [[75],
        [95,64],
        [17,47,82],
        [18,35,87,10],
        [20,4,82,47,65],
        [19,1,23,75,3,34],
        [88,2,77,73,7,63,67],
        [99,65,4,28,6,16,70,92],
        [41,41,26,56,83,40,80,70,33],
        [41,48,72,33,47,32,37,16,94,29],
        [53,71,44,65,25,43,91,52,97,51,14],
        [70,11,33,28,77,73,17,78,39,68,17,57],
        [91,71,52,38,17,14,91,43,58,50,27,29,48],
        [63,66,4,68,89,53,67,30,73,16,69,87,40,31],
        [4,62,98,27,23,9,70,98,73,93,38,53,60,4,23]]
new = []
new_1 = []
for num in range(0,14):
    control = all[13][num]
    ln = all[14][num]
    rn = all[14][num+1]
    if control +ln>control+rn:
        new.append(control+ln)
    else:
        new.append(control+rn)
print(new)

for num in range(12, -1,-1):
    new_1 = new
    new = []
    for num_1 in range(0, num+1):
        control = all[num][num_1]
        ln = new_1[num_1]
        rn = new_1[num_1+1]
        if control +ln>control+rn:
            new.append(control+ln)
        else:            
            new.append(control+rn)
    print(new)













