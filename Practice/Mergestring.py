def merstr(s1,s2):
    ss1=list(s1)
    ss2=list(s2)
    out=[]
    l1=[]
    if(len(ss1)==len(ss2)):
        for i in range(0,len(ss1)):
            out.append(ss1[i]+ss2[i])

    elif(len(ss1)>len(ss2)):
        s=abs(len(ss1)-len(ss2))
        for i in range(0,len(ss2)):
            out.append(ss1[i]+ss2[i])
        j=1
        while(j<=s):
            l1.append((ss1[-j]))
            j=j+1
        a="".join(l1)
    else:
        s=abs(len(ss1)-len(ss2))
        for i in range(0,len(ss1)):
            out.append(ss1[i]+ss2[i])
        j=1
        while(j<=s):
            l1.append(ss2[-j])
            j=j+1
            a="".join(l1)







    out = "".join(out)
    return out+a[::-1]

print(merstr('abt','dfeop'))