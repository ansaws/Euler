from Lib.divisors import divisors
s = []
ab = []
tot = 0
for i in range(2,28124):
	if sum(divisors(i))>i:
		ab.append(i)
	else:
		continue
for f in ab:
	for t in ab:
		if t+f<28124:
			s.append(t+f)
s= set(s)
for num in range(1, 28124):
	tot += num
print(tot-sum(s))
