from Lib.ISPRIME import isPrime
"""
n2= 10
answer = []
ans = 0
count = 0
max_count = 0
max_num = 0
thing = 0
for n1 in range(9,1001,2):
  while n1 > n2:
    n2 = n2*10   
  while True:
    while n1> n2:
      n2 = n2*10
      answer.append(0)
    if n2%n1 == 0:
      count = 1
      break
    ans = n2//n1
    n2 =n2 - (n1*ans)
    for yeet in range(0, len(answer)-1):
      if answer[yeet] == ans:
        thing = yeet
        break
    if ans in answer:
      del answer[:thing]
      break
    else:
      answer.append(ans)
  if count ==1:
    continue
  if len(answer)> max_count:
    max_count = len(answer)
    max_num = n1
  count = 0
  n2 = 10
  answer = []
"""
n2 = 10
digits = []
digit = 0
max_count = 0
for n1 in range(2,1000):
  n2 = 10
  while True:
    if n1>n2:
      n2*=10
    while n1>n2:
      n2*=10
      digits.append(0)
    if n2%n1==0:
      break
    digit = n2//n1
    n2-= digit*n1
    digits.append(digit)
    if digits.count(digit)>1:
      digits.pop()
      if len(digits)-digits.index(digit) >max_count:
        max_count = len(digits)-digits.index(digit)
      break
  digits = []
print(max_count)
    