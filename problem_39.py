side1 = 1
side2 = 1
hyp = 0
sol = 0
final = 0
ans = 0
for tri in range(3,1000):
    for side1 in range(1, tri):
        for side2 in range(side1, tri):
            hyp = tri-(side1+side2)
            if hyp<0:
                break
            elif side2+side1<hyp:
                continue
            elif side1**2+side2**2==hyp**2:
                sol+=1
    if sol>final:
        final = sol
        ans = tri
    sol = 0
print(ans)