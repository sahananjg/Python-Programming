def RWIS(string):
    a=[]
    word=string.split(" ")
    word.reverse()
    for i in word:
        if(i!=""):
            a.append(i)
    a=" ".join(a)

    return a
print(RWIS("  Bob    Loves  Alice   "))