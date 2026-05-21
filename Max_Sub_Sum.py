Arr=[-2,1,-3,4,-1,2,1,-5,4]
Ma=float('-inf')
ca=0
for i in range(len(Arr)):
    ca+=Arr[i]
    Ma=max(Ma,ca)
    if(ca<0):
        ca=0
print(Ma)        