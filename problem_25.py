#sucess
a=1
b=2
c = None
d = 3
while True:
    c = a+b
    a=b
    b=c
    d+=1
    if len(str(b)) == 1000:
        print(b)
        print(d)
        break 



