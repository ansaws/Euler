from Lib.divisors import divisors
s = []
ab = []
tot = 0
for i in range(2,28123):
	if sum(divisors(i))>i:
		ab.append(i)
	else:
		continue
for f in ab:
	for t in ab:
		if t+f<28123:
			s.append(t+f)
s= set(s)
for yeet in range(1, 28124):
	tot += yeet
print(tot-sum(s))
