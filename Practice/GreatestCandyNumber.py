def CN(num:list[int],n:int) -> list[bool]:
    m=max(num)
    a=[]
    for i in range(len(num)):
        if(num[i]+n>=m):
            a.append(True)
        else:
            a.append(False)
    return a
print(CN([2,3,5,1],3))




