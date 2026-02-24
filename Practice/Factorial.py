''''For loop
def fac(n):
    if (n ==0):
        return 1
    else:
        f=1
        for i in range(1,n+1):
            f=f*i
        return f
# Recursion function
def Rfac(m):
    if (m == 0):
        return 1
    else:
        return m*Rfac(m-1)
n=int(input("Enter a number: "))
if(n <0):
    print("Sorry, you can't be less than zero")
else:
    print("The value by using for loop:",fac(n))
    print("The value by using recursion function:",Rfac(n)) # The function call itself '''
n=int(input())
j=0
L=[0 for i in range(n)]
for i in range(n):
    a=int(input())
    if a!=0:
        L[j]=a
        j+=1
for i in L:
    print(i,end=" ")