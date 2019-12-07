#succes
import datetime
s = 0
for year in range(1901, 2001):
	for month in range(1,13):
		if month ==2 and year%4  == 0 and year!=1900:
			for day in range(1, 30):
				d = datetime.date(year, month, day)
				if d.weekday() == 6 and day == 1:
					s+=1	
		elif month ==2:
			for day in range(1,29):	
				d = datetime.date(year, month, day)
				if d.weekday() == 6 and day ==1:
					s+=1
		elif month == 9 or month == 4 or month == 6 or month ==11:
			for day in range(1,31):
				d = datetime.date(year, month, day)
				if d.weekday() == 6 and day ==1:
					s+=1
		else:
			for day in range(1, 32):	
				d = datetime.date(year, month, day)
				if d.weekday() == 6 and day ==1:
					s+=1
print(s)

			
