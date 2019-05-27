#sucess
def permutations(lst):
    if len(lst) == 0:
        return []
    
    if len(lst) == 1:
        return[lst]

    remlst = []
    l = []
    for i in range(0, len(lst)):
        m = lst[i]
        remlst = lst[:i] + lst[i+1:] 
        for p in permutations(remlst):
            l.append([m] + p)
    return l
data = list('0123456789') 
x= permutations(data)
print (x[999999])
