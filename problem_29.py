num = []
total = 0
for x in range(2, 101):
	for y in range(2, 101):
		num.append(x**y)
mylist = list(dict.fromkeys(num))
print(len(mylist))