def Posneg():
    n=int(input("enter the number"))
    m=n-1
    if(n==0):
        print("Already Zero")
    elif(n>0):
        while(m>=0):
            print(m)
            m-=1

    else:
        while(n<=0):
            print(n)
            n+=1
        
Posneg()      
