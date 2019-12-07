from divisors import *
ab = []
s = 0
tot = 0
for i in range(2,28123):
	if sum(divisors(i))>i:
		ab.append(i)
	else:
		continue
for f in ab:
	for t in ab:
		s += t+f
for yeet in range(1, 28124):
	tot += yeet
print(tot-s)
