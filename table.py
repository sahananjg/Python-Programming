def multiplicationTable():
    N=int(input("enter the number"))
    m=0
    for i in range(1,11):
        m=i*N
        print(i,"X",N,"=",m)
        
multiplicationTable()

