def fib(n):
    a,b=0,1
    if (n == 0):
        print(a)
    elif n<0:
        print("Enter a eiligible value" )
    else:
        print(a)
        print(b)
        for i in range(2,n):
            c=a+b
            a,b=b,c
            print(c)
n=int(input("Enter a number: "))
fib(n)