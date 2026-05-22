n=int(input())
a,s=[],[]
def BT(open,close):
    if len(s)==2*n:
        a.append(''.join(s))
        return
    if open<n:
        s.append('(')
        BT(open+1,close)
        s.pop()
    if open>close:
        s.append(')')
        BT(open,close+1)
        s.pop()
BT(0,0)
print(a)            