def isPerm(num, num2, num3):
    num = list(str(num))
    num2 = list(str(num2))
    num3 = list(str(num3))
    if len(num) == len(num2) == len(num3):
        for i in range(0, len(num)):
            num[i] = int(num[i])
            num2[i] =  int(num2[i])
            num3[i] = int(num3[i])
        if sorted(num) == sorted(num2) == sorted(num3) ==sorted(list(set(num))):
            return True
        thingy = list(set(num))
    return False
