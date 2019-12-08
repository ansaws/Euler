from Lib.divisors import divisors as d
su = 0
for a in range(1,10001):
    b = sum(d(a))
    if (a == sum(d(b))and (a != b)):
        su += a
print(su)




