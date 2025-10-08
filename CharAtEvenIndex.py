def stringJumper():
    s=str(input("enter a string:"))
    for i in range(0,len(s)-1):
        if(i%2==0):
            print(s[i], end="")
            
        #printing character and separating characters by nothing
stringJumper()
